from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the Excel data
df = pd.read_excel("APEAPCET2023LASTRANKDETAILS.xlsx")
df = df.loc[:, ~df.columns.str.contains('^Unnamed|^\\s+$')]  # Remove unnamed or blank columns

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Get user input
        rank = int(request.form['rank'])
        gender = request.form['gender'].upper()           # MALE or FEMALE
        raw_category = request.form['category'].upper()   # e.g., OC, SC, EWS

        # 2. Adjust category for EWS
        category = "OC_EWS" if raw_category == "EWS" else raw_category

        # 3. Construct cutoff column name
        col_name = f"{category}_{'BOYS' if gender == 'MALE' else 'GIRLS'}"

        # 4. Check column existence
        if col_name not in df.columns:
            return f"❌ Error: Column '{col_name}' not found in dataset. Please check the inputs.", 400

        # 5. Convert column to numeric and clean cutoff values
        df[col_name] = pd.to_numeric(df[col_name], errors='coerce')  # Convert strings like '--' or 'NA'
        df[col_name] = df[col_name].replace([0, '0'], pd.NA)         # Replace 0 and '0' with NaN

        # 6. Filter by rank
        filtered = df[df[col_name].fillna(9999999) >= rank]
        filtered = filtered[filtered[col_name].notna()]  # Ensure valid cutoff exists

        # 7. Apply optional filters
        branch = request.form.get('branch')
        district = request.form.get('district')
        college_type = request.form.get('college_type')

        if branch:
            filtered = filtered[filtered['branch_ code'].str.contains(branch, case=False, na=False)]
        if district:
            filtered = filtered[filtered['DIST'].str.contains(district, case=False, na=False)]
        if college_type:
            filtered = filtered[filtered['TYPE'].str.contains(college_type, case=False, na=False)]

        # 8. Prepare output
        output = filtered[[
            'NAME OF THE INSTITUTION', 'branch_ code', 'DIST', 'TYPE', col_name, 'COLLGE_FEES'
        ]].rename(columns={
            'NAME OF THE INSTITUTION': 'College Name',
            'branch_ code': 'Branch',
            'DIST': 'District',
            'TYPE': 'College Type',
            col_name: 'Last Year Cutoff',
            'COLLGE_FEES': 'College Fees'
        })

        return render_template('results.html', tables=output.to_dict(orient='records'))

    except Exception as e:
        return f"⚠️ An unexpected error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

