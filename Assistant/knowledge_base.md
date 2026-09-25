# About AsphaltMine

AsphaltMine is an online database of asphalt test results. People enter or upload asphalt mixture and test data, search and download records, look at live statistics, and use trained machine learning models to predict asphalt properties from mixture information.

The six test types stored in AsphaltMine are the Rutting Test, the Marshall Test, the Indirect Tensile Strength Test (ITS), the Thermal Stress Restrained Specimen Test (TSRST), the Uniaxial Tension Stress Test (UTST) and the Stiffness Test. Every record also describes the data source (who measured it and where it was published) and the asphalt mixture (recipe, materials, mixing and recovered materials).

Quick summary of who can do what:

- Without an account, visitors can use only the Visualization page, the Prediction page and the FAQ. Every other page, including Database, Data Curation, Bulk Upload, My Data, Shared Workspaces and My Account, requires logging in.
- Any logged in user can search, view and download the records they are allowed to see.
- Saving records through Data Curation or Bulk Upload needs curate (write) access. New accounts do not have it, and it can be requested from the My Profile page with the Request Write Access button.
- Records are private to their owner unless they are placed in a shared or public workspace.

Two prediction models are available today: Marshall (predicts Marshall Stability and Flow) and Volumetric Properties (predicts Bulk Density and Air Voids). Prediction for the other tests is planned.

To request write access, open My Account, then My Profile, and click Request Write Access. For questions this assistant cannot answer, users can write to contact@asphaltmine.org.

# The AsphaltMine Project

AsphaltMine is a research project of the Empa Concrete and Asphalt Laboratory in Switzerland (Empa is the Swiss Federal Laboratories for Materials Science and Technology). Its goal is to collect asphalt test results in one organized online database and to use this data to train machine learning models that predict asphalt performance. Predicting laboratory test results from results at a lower scale, for example the rutting test result from the component material test results and their proportions, can reduce the amount of physical testing needed and support better mixture design. The stated vision is that AsphaltMine becomes a perpetual asphalt community project that keeps collecting new data, building new tools and updating the existing ones.

The project website is asphaltmine.org. Its menu has Home, News, About AsphaltMine, Data Structure, Participants, Join and Data Portal. The home page states more than 3000 test results, 6 participating countries and 2 prediction models available. The database and tools described in this guide (data entry, search, visualization and prediction) run on the AsphaltMine data portal, which is opened with the Log In or Data Portal link on the project website.

People:
- Martins Zaumanis is the principal investigator and a scientist at the Empa Concrete and Asphalt Laboratory.
- Mohammad Abbas is a postdoctoral researcher at Empa who leads the development and does the main work on the database and the machine learning models.

Funding and partners: the work is funded by Swiss National Science Foundation project No. 213163, "Fate of Polymers in Recycled Asphalt", a four year project. It is a collaborative project with the University of Antwerp and Vienna University of Technology (TU Wien), whose partners contribute expertise and resources to building and populating the database.

Participants: European companies and academic institutions with reliable asphalt test results are invited to contribute data. Current participating organizations come from Switzerland, Austria, Belgium, Serbia, Latvia and Lithuania, and include private companies, research labs and universities. Contributors get access to the prediction tool.

Data sharing: the web platform allows full customization of access rights. If a contributor does not wish to share results publicly, they remain undisclosed and are used only to build the prediction tool, never shared with the public. Only reliable results should be collected, and unsatisfactory results (samples that do not pass the requirements) can also be included, with the option not to disclose them. Depending on the partner's requirements, an individual data sharing agreement can be prepared.

Technology and standards: the data is stored in a structured XML format on the open source Configurable Data Curation System, and the database structure follows European (EN) testing standards so it can be used across European countries. By default the data is stored on a server in Switzerland. Data can be entered through web forms or uploaded in bulk from an Excel sheet, and for standardized test result protocols (pdf or Excel files) a plug-in for automatic uploading can be developed case by case. Results can be downloaded and converted back to Excel. The database is planned to grow beyond the six current tests, and suggestions for other test methods are welcome.

Prediction models: in January 2026 the project published its first prediction tool, a physics based machine learning model for predicting Marshall test results that combines a data driven approach with physical constraints to improve reliability and interpretability. Marshall was chosen because the most data was available, and the approach is intended to be extended to other asphalt tests. The paper describing it has the DOI 10.1016/j.cscm.2026.e05829. The prediction tools are accessed in the data portal.

Citing and acknowledging: anyone who publishes work that uses AsphaltMine data or tools is asked to acknowledge the data contributors in the acknowledgement section of the publication.
Contact: the AsphaltMine team can be reached by email at contact@asphaltmine.org. This is the address for joining the project, contributing data, giving feedback, asking about participation, or any question this assistant cannot answer. There is no contact form. Write access is requested from the My Profile page, not by email.

About this assistant: it is an AI helper built into the AsphaltMine website by the AsphaltMine team to answer questions about using the website and about the tests, data fields and prediction models. It can make mistakes, so important details should be checked with the project team. It remembers the current conversation (roughly the last eight exchanges) only in your own browser tab while the tab stays open; the refresh button in the chat header (tooltip "Start a new chat") clears it, and the assistant does not keep a history of your chats between visits. Each question, together with that recent conversation, is sent to Google's Gemini AI service to produce the answer, so do not type passwords or confidential information into the chat. To keep it available for everyone, it limits how many questions one person can ask per hour, and visitors who are not signed in can ask fewer questions than signed in users, so signing in gives you more; if the limit is reached it tells you so and asks you to sign in or try again a little later.

When the user writes a field name from the data structure such as MeasurementCampaignID, note that on the Data Curation form the same field appears with spaces, for example Measurement Campaign ID.

# AsphaltMine User Guide

AsphaltMine is a website for collecting asphalt test results in an organized online database, exploring them, visualizing them, and using them for prediction. This guide explains how to use each page, using the names of buttons, tabs and menus exactly as they appear on screen.

## 1. The top navigation menu

The menu bar sits at the top of every page. The logo and name are at the far left and all the menu links are grouped on the right. From left to right it contains the following items.

1. **AsphaltMine** (logo and name at the far left, with the small caption Data Portal). Opens the AsphaltMine project website in the same window.
2. **Data Curation**. The form where you type in a new test record, load a record, or edit one of your records. Login is required.
3. **Bulk Upload**. Lets you add many records at once from a predefined Excel sheet. Login is required.
4. **Database**. Search and explore all records you are allowed to see, and download them. Login is required.
5. **My Data**. The list of records you own, with actions such as view, edit, delete and move to a workspace. Login is required.
6. **Shared Workspaces**. The workspaces you own or that were shared with you, plus their contents. Login is required.
7. **Visualization**. Charts and statistics summarizing the database (General and Live Insights tabs). It can be opened without logging in.
8. **Prediction**. Machine learning models that predict test results from mixture properties. It can be opened without logging in.
9. **Publications**. A page for the project's published papers. For now it says "Coming soon". It can be opened without logging in.
10. **My Account** or **Log In / Sign Up** (far right).

The **FAQ** (frequently asked questions) is not in the top menu. It is linked as **FAQ** in the footer at the bottom of every page, and it can be opened without logging in.

If you are not logged in, the far right item reads **Log In / Sign Up**. It opens the login page, which also links to account creation.

If you are logged in, the far right item is **My Account**, a dropdown with these entries:

- **File Attachments**: your uploaded files.
- **My Profile**: your account details and settings.
- **Administration**: shown only to administrators (staff accounts).
- **Logout**: ends your session.

On a small screen the menu is hidden behind a three-line menu button at the top. Tap it to open the list, and tap My Account to open its dropdown.

The page you are on is highlighted in the menu.

Pages that require login send you to the login page if you are not logged in. After logging in, you are taken back to the page you asked for, or to Data Curation by default.

## 2. Accounts: signing up, logging in, resetting a password, and access levels

### Signing up

1. Click **Log In / Sign Up** in the top menu.
2. On the login page, click **Create Account**.
3. On the **Create Account** page, fill in the fields. Fields marked with a red asterisk are required:
   - **Username**
   - **First Name**
   - **Last Name**
   - **Email Address**
   - **Password**
   - **Password confirmation** (type the same password again)
   - The captcha (type the characters shown in the image).
4. Click **Create Account**.
5. The **Check Your Email** page appears. It says a verification link was sent to your address. Open your email and click the link, which activates your account. If you do not see the email, check your spam or junk folder.
6. When the link works, the **Email Verified** page says your account is active. Click **Log In** on that page to sign in.

Rules and messages you may meet while signing up:

- The email address must not already belong to another account. Otherwise you see "A user with that email already exists."
- Password rules, as enforced by the website: at least 8 characters, at least one uppercase letter, at least one lowercase letter, at least one digit, at least one non-alphanumeric character (a symbol), fewer than 5 occurrences of the same character, not a very common password, not entirely numeric, and not too similar to your personal details. The rules are also listed under the password box.
- If the verification link is invalid or has expired, the **Verification Failed** page appears with a **Resend Verification Email** button.

### Resending the verification email

1. On the **Check Your Email** page, click **Didn't get it? Resend the email**. You can also reach this page from the login page when it says your email address is unverified (click **Resend the verification email**).
2. On the **Resend Verification Email** page, type the email you signed up with, complete the captcha, and click **Resend Email**.
3. Use **Back to login** to return to the login page.

### Logging in

1. Click **Log In / Sign Up**.
2. On the **Login** page ("Sign in to AsphaltMine"), type your username and password, then click **Login**.
3. If the details are wrong you see "Invalid username and/or password. Please try again or write to contact@asphaltmine.org for assistance."
4. If your email is not yet verified, the page says "Your email address is still unverified" and offers a link to resend the verification email.
5. After several failed attempts in a row, the site may show "Account Locked. Too many login attempts. Please try again later." Wait and try again.

To sign out, open **My Account** and click **Logout**. On the online portal you are also signed out when you close the browser, and a login lasts at most 7 days. Some browsers can bring your login back when they reopen if they are set to continue where you left off.
### Forgot password and password reset

1. On the login page, click **Forgot password**.
2. On the **Forgot password** page, type your email and click **Send reset link**.
3. The **Check your email** page tells you that instructions were sent if an account exists for that address. Check your spam folder if nothing arrives.
4. Open the email and click the link. The **Set new password** page appears.
5. Enter the new password (the same password rules apply) and click **Change password**.
6. The **Password reset complete** page appears. Click **Sign in**.

If the reset link was already used or is invalid, the page says so and offers **Request a new link**.

### Read-only access and write access

- A newly created account is read-only. The Create Account page says write access can be requested from My Profile once logged in.
- With read-only access you can log in, use the Database page to search and view records, and use Visualization and Prediction.
- Saving records (from Data Curation or Bulk Upload), extracting and validating Excel sheets, and updating records need curate (write) access. Without it, these actions fail with messages such as "Insufficient Permission." (Data Curation) or "Insufficient permissions" (Bulk Upload).
- To request write access, open My Account, then My Profile, and click Request Write Access next to the Write Access row. Fill in Organization name (Institute, company or university), Country or countries (source of data), the standards followed for the data (European standards, or Other with a field to specify which) and a short Description, then click Send Request. The AsphaltMine team reviews the request; if accepted, an email confirms that write access was granted, and if denied you keep read-only access and can send a new request.
- Access to workspaces is a separate matter. In a workspace you can be given read access (view) or write access (add and edit records). See section 6.
- Data Curation and Bulk Upload pages open once you are logged in, but for accounts without curate access the save, extract and validate actions are refused.

## 3. Data Curation: entering, loading, editing and saving records

Data Curation (the GV Web Form) is where you type in one record at a time. Login is required.

### Screen layout

- **Left sidebar** titled "GV Web Form": links that jump to each section. The main sections are **Data Source**, **Mixture**, **Results** and **Notes**. Mixture and Results expand into sub-links (for example Mixture Identifiers, Mixture Recipe, Mixture Component Properties, Recovered Materials and Mixing under Mixture, and Sample Properties and Test Results under Results). Arrow buttons at the bottom of the sidebar jump to the top or bottom of the page.
- **Right sidebar**:
  - **Performance Tests** box showing the currently selected test (Rutting Test by default). Click it to change the test selection.
  - **Functionalities** list with four question mark help icons: Save new records, Load and View records, Update existing records, Download records.
  - A note that fields marked with a red asterisk are required, and a note about semi-mandatory fields (with a help icon).
  - **Quick Start** button, which opens a short step by step guide on top of the page, with a link to the FAQ and a button that opens Ask AsphaltMine.
- **Upload Form** panel at the top of the form, used to load an existing record (see "Loading a record").
- Form sections with **Show** tabs. Sections start collapsed. Click a tab to open a section (main sections use a tab labelled **Show**, inner sections use a tab carrying their name, such as **Mixture Identifiers**). Click the minus sign in a section title to hide it again.
- **Download** and **Save** buttons at the bottom of the form (in edit mode these are replaced by **Update**).

Screen size: the form needs a window at least 800 pixels wide to work and 1400 pixels for full functionality. On a smaller screen a message says "Your screen size is too small to display the form properly." Between 800 and 1400 pixels wide, the test selection box moves into the form area.

### Choosing the test or tests

1. Click the box under **Performance Tests** on the right (it shows "Rutting Test" at first).
2. In the **Select Performance Tests** popup, tick the tests you want. The choices are:
   - Rutting Test
   - Marshall Test
   - Indirect Tensile Strength Test (ITS)
   - Thermal Stress Restrained Specimen Test (TSRST)
   - Uniaxial Tension Stress Test (UTST)
   - Stiffness Test
3. Click **Apply**. The form now shows the fields for the tests you chose. The box on the right lists them, for example "Rutting + Marshall Tests".

You can select several tests at once. The Data Source and Mixture sections are shared, and each test gets its own Sample Properties block and its own Test Results block (tabs named after the test, such as "Marshall Test"). One separate record is saved per selected test.

### Filling in the form

Fields marked with a red asterisk are required. Hover or click the small information icon next to a field label for an explanation and an example value. Number fields show a hint if the entry is not valid, for example "Enter a valid number between 0 and 100." or "Enter a valid positive number."

**Data Source** (open it with **Show**):

- Required: **Measurement Campaign ID**, **Organization Name**, **Location Country**, **Year**.
- **Data Record Type** has two choices: **Complete Data Record** or **DOI Identifier Only**. With DOI Identifier Only, type the DOI. With Complete Data Record, pick a **Complete Record Type** (Journal Article, Article in Conference Proceedings, Book Publication, Published Report, Unpublished Report, or Other Bibliographic) and fill in the bibliographic details such as First Author, Co-Authors (separate names with semicolons), Article Title, Journal Title, Year, Publisher, DOI and similar fields.
- **Data Source Notes** is a free text note.

**Mixture**:

- **Mixture Identifiers**: **Mixture ID** and **Mixture Type** (Mixture Type is required, for example AC B-32).
- **Mixture Recipe**: **Composition** (Aggregates Grain Size Distribution, Virgin Filler, Recovered Filler, Reclaimed Asphalt, Target Binder Grade, Binder Content) and **Mixture Maximum Density**.
- **Mixture Component Properties**: separate sub-sections for Virgin Aggregates, Filler, Virgin Binder, Additives, Reclaimed Asphalt Aggregates, Reclaimed Asphalt Binder, Pre-mixing Binder Blend and Other Materials. Many have their own inner tabs such as Viscosities, BTSV, MSCRT, Aging Resistance and Additional Properties. Use **+ Property** (or **+ BTSV Property**) to add extra measured properties, and **Add New Additive** to add another additive.
- **Recovered Materials**: Recovered Aggregates and Recovered Binder.
- **Mixing**: **Mixing Method** is required (Laboratory hand mixing, Laboratory mechanical mixing, or Plant mixing). Other fields include Type of Mixer, Mixing Sequence, temperatures and duration. **Mixture Notes** holds a free text note.

**Grain size distributions**: each distribution has two boxes, **Size (mm)** and **Proportion (%)**. Type the values separated by semicolons, in matching order, for example sizes "0.063; 0.5; 2" and proportions "8; 20; 40". Both boxes must contain the same number of values. Click the chart button (the small graph icon, tooltip "Show or hide plot.") to draw the curve and check it.

**Results**:

- **Sample Properties**: **Sample Preparation** (Pavement Coring or Loose Mixture), coring or compaction details, and **Mixture Aging** where relevant.
- **Test Results**: the required fields depend on the test:
  - Rutting Test: **Test Temperature** and **Method of Measurement** (choose Large or Extra-Large Devices, Small Size Device in Air Method A, Small Size Device in Air Method B, or Small Size Device in Water Method B). Then the required mean results for that device type (for example Mean Thickness, Number of Cycles, and Mean Proportional Rut Depth or Mean Rut Depth) and a bulk density **Method of Measurement**. Use the **+ Replication** button to add replicate results.
  - Marshall Test: **Corrected Stability (kN)**, **Flow (mm)** and the bulk density **Method of Measurement**.
  - Indirect Tensile Strength Test: **Test Temperature**, **Indirect Tensile Strength (kPa)** and the bulk density **Method of Measurement**. A **Wet** tab and replication buttons are available.
  - TSRST: Start Temperature, Temperature Rate, Failure Stress, Failure Temperature and the bulk density **Method of Measurement**.
  - UTST: Test Temperature, Applied Deformation Rate, Tensile Strength and Failure Strain.
  - Stiffness Test: **Test Type**, **Test Temperature** and **Stiffness Modulus (MPa)**. Use **Add New Temperature** to add more temperatures.

**Notes**: **General Notes** is a free text note about the experiment.

Semi-mandatory fields: at least one entry of each of the following should be filled for a useful record, although the form does not block saving without them. Grain Size Distribution: Virgin Aggregates or Recovered Aggregates. Binder Content: Binder Content in Mixture Recipe or Percentage Content of Recovered Binder. Penetration: Virgin Binder Penetration or Recovered Binder Penetration. Voids: Bulk density with Maximum density, or Air voids.

### Saving a new record to the database

1. Choose the test or tests (see above) and fill in the form, especially all required fields.
2. Click **Save** at the bottom of the form.
3. A confirmation box says: "This action will save the record to the database. Confirm save?" It also shows **Assign to a workspace** with a dropdown that starts as **Keep private (no workspace)**. Open it to pick a workspace instead. The list contains workspaces you own or can write to. Public workspaces are marked "(public)".
4. Click **Confirm** (or **Cancel** to go back).
5. All sections open so the browser can flag anything missing. If a required field is empty, the browser highlights it and the record is not saved. Fill it in and click **Save** again.
6. On success a popup says "Record Saved." (and "Assigned to <workspace name>" if you picked one).

Other popups you may see after saving:

- "Failed to save record."
- "Insufficient Permission." (your account does not have curate access)
- "<n> of <total> records saved, <k> failed." (when several tests were selected and only some were saved)
- "Record Saved." with a warning: "<n> of <total> records could not be moved into <workspace>." or "Saved, but could not be moved into <workspace>."

Notes about saving:

- Records are stored in the database as structured documents. If you selected several tests, several records are created.
- The record name is built from the Measurement Campaign ID, Organization Name and Year, followed by a unique number.
- With **Keep private (no workspace)** a record is visible only to you. See section 6 for workspaces and sharing.
- Save before leaving the page. Unsaved entries are lost when you leave.

### Downloading a record as a file

1. Fill in a new record or load an existing one.
2. Click **Download**, then **Confirm** in the box that says "This action will download the record to your device in XML format. Confirm download?"
3. If all required fields are valid, the file downloads immediately and the popup says "Record Downloaded." If several tests are selected and completed, several files download. The file name is built from the Measurement Campaign ID, Organization Name and Year.

### Loading a record (from the database or from your device)

Use the **Upload Form** at the top of the page.

1. Choose a source:
   - **Choose Record from AsphaltMine Database**: this takes you to the Database page. Click the title of a record there. You return to Data Curation with the record name shown in bold in this box and the matching test already selected.
   - **Choose Record from your own Device**: pick an XML file that you downloaded earlier from the form.
2. Under **Select elements to upload**, tick the parts you want: **Data Source**, **Mixture**, **Sample Properties**, **Results**, **General Notes**, or **All Elements** (everything is ticked by default).
3. Click **Load**.
4. The form fills in. Click the chart button next to grain size and result curves to view graphs.

If you click **Load** without choosing a record, a popup titled **Incorrect Entry** says "Please select a record to upload". Loading fills the form only. It does not change the stored original. If you then click **Save**, a new record is created.

### Viewing an existing record

There are two ways to view a record in the form. On the Database page, click the record title. On My Data, open **Actions** for the record and click **View**. Both open Data Curation with the record loaded, as described above.

### Editing one of your existing records

1. Go to the Database page or My Data.
2. On the Database page, click the pencil icon (tooltip "Edit") beside the record. The pencil appears only for records you are allowed to edit. The sidebar notes that you must be the owner of the record. On My Data, open **Actions** and click **Edit** (it is greyed out when you may not edit).
3. Data Curation opens in edit mode. A banner reads Editing Record with the record name and test, and a **Cancel** link (tooltip "Exit edit mode without saving") returns you to the Database page.
4. The Upload Form, **Save** and **Download** buttons are replaced by a single **Update** button. The test type is locked: you cannot change it. To change the test type, load the record and save it as a new record with the other test.
5. Change, delete or add entries.
6. Click **Update**, then **Confirm** in the box that says "This action will update the record in the database. The action is irreversible. Confirm update?"
7. After you confirm, the page goes straight to the Database page. No success message is shown, so search for the record there to check your change.

### Validation messages

If a required field is empty or wrongly formatted, the browser highlights the field and shows a tooltip. Save, Download and Update do nothing until every required field is valid. A popup titled **Incorrect Entry** appears for list style entries. Examples:

- "Aggregates distribution mismatch: Size and Proportion values must have the same count."
- "Invalid Size in Aggregates: <value>" or "Invalid Proportion in Aggregates: <value>" (sizes must be positive numbers, proportions between 0 and 100).
- The same style of message for Virgin Aggregates, Reclaimed Aggregates and Recovered Aggregates, and for the graph values of rutting and TSRST results (for example, "Rut Depths and Cycles values must have the same count.").

## 4. Bulk Upload: many records from an Excel sheet

Bulk Upload adds many records at once. It needs login and curate (write) access.

### Getting the Excel template

On the left of the page, the **About this page** box says "Bulk upload records using the predefined AsphaltMine Excel sheet" and offers a link named **here** to download the predefined Excel file. The **Reset** button (circular arrow, tooltip "Reset the page") in that box clears the page and starts over. You can also open the **Quick Start** button on the right for a short step by step guide.

Another way to get a correctly formatted file: on the Database page or My Data, choose **AsphaltMine Format (.xlsx)** when downloading, as it is compatible with AsphaltMine upload (section 5).

### Filling the sheet

- The sheet has header rows describing each field, and each record occupies one row (Database Columns sheet) or one column (Database Rows sheet). Records start below the header block.
- Where a field holds several values (for example grain sizes and proportions), values are separated by semicolons.
- The server rejects uploaded files larger than about 10 MB. If your Excel file is bigger, split it into several files and upload them one after another.
- One row can contain results for more than one test. One record is created per test that has results. For example, a row with Marshall and ITS results becomes two records.

### The steps

1. Click **Upload AsphaltMine Excel File** and choose your Excel file (.xls or .xlsx). The label changes to "Excel File Uploaded".
2. Under **Sheet**, choose **Database (Columns)** or **Database (Rows)**, whichever matches the layout of your file.
3. Click **Extract**, then **Confirm** in the box that says "This action will extract records from the uploaded Excel sheet, which may take some time. Confirm extraction?" (Extract stays greyed out until a file is chosen.)
4. While it works you see "Extracting records, please wait...". Then either "Extraction successful" with the number of records extracted, or "No records to extract."
5. After a successful extraction a **Validate** button appears. Click it, then **Confirm** ("This action will check the validity of all records. Confirm?").
6. Validation shows "Validating records, please wait..." and then one of two outcomes:
   - "All <n> records are valid." The workspace choice and the **Save** button appear.
   - "<n> of <total> records are invalid. Please review your Excel sheet." Each invalid record is listed by name, for example "Row 12 - Marshall" (or "Column 'L' - Marshall" for the Rows sheet), with the reason.
7. Optionally choose a workspace: under **Assign all records to a workspace**, open the dropdown (it starts as **Keep private (no workspace)**) and choose a workspace. Public workspaces are marked "(public)". Only workspaces you own or can write to are listed.
8. Click **Save**, then **Confirm**. The message says either "This action will save all records to the database, visible only to you. Confirm save?" or, if a workspace was chosen, "This action will save all records to the database and assign them to the workspace "<name>". Confirm save?"
9. The result reads "All <n> records saved successfully." (with "Assigned to <workspace>" if applicable). If some fail you see "<x> saved, <y> failed." with the failed records listed, and possibly "<n> of <total> records could not be moved into <workspace>."

The buttons appear step by step: Extract, then Validate, then Save. Save only appears when every record is valid, so you must fix the Excel file and start again if any record is invalid: correct the sheet, upload it again, then Extract and Validate once more. Records are saved in batches, so a large file may take a while.

### Typical errors and what they mean

Validation reasons are written as "INVALID:" followed by a short description and the location in the record:

- **Missing field '<name>'. Check field at: ...** A required value is empty in your sheet. Fill in the column for that field.
- **Incorrect field format. Check field at: ...** A value does not match the expected format, for example text in a number cell or a value outside the allowed range.
- **Incorrect integer format.** A whole number was expected.
- **Incorrect date format.** A date was expected in the correct date format.
- **XML syntax error** or **Unexpected error**: the row could not be turned into a record, usually because of a badly structured cell such as a broken list of values. Check the cell against the template.
- "Check field at" shows the place in the record, using names such as Mixture, DataSource and the test name.

Other messages:

- "Insufficient permissions": your account has no curate access. Request it from My Profile.
- "No records to extract.": the chosen sheet has no records. Check that you picked the right sheet (Columns or Rows) and that data starts in the expected place.
- Any other message after Extract is shown as the server's own error text. Re-check the file and sheet.
- After saving, the records appear on the My Data page.

## 5. Database: search, view and download records

The Database page lets you find records and download them.

### Searching

1. Click **Database** in the top menu.
2. Click the search box. Its hint reads "Search records, or leave blank for all".
3. Type a word and press Enter (or the space bar) to turn it into a keyword tag. Suggestions appear after two characters. You can add several keywords. A record must contain all of the keywords to match.
4. The search runs automatically about three seconds after you add a keyword. You can also click the magnifying glass button (tooltip "Search") to run it right away. Searching with no keywords lists every record you may see.
5. Remove a keyword by clicking the small cross on its tag.

### Filtering

On the left, filters narrow the results:

- **Filter by Test**: tick the tests you want (pill buttons). **Select All** ticks all of them, then reads **Unselect All**.
- **Filter by Workspace**: shown when you have access to at least one workspace. Click the box (hint "Search workspaces…"), type to find a workspace, and click it to add it as a chip. Include **No Workspace** to see records that are not in any workspace. **Clear all** removes the chips.

If the results do not change after you adjust a filter, click the magnifying glass button to run the search again.

### Reading the results

- Results appear in a tab labelled "From <source name>" with a count badge and the word **Records**.
- Each row has a checkbox, an arrow to expand or collapse the record details, the record title, the test name and the last modification date. A **file** badge shows when a file is attached. A pencil icon (tooltip "Edit") appears when you can edit the record.
- Clicking the record title opens the record in the Data Curation form (section 3), where you can inspect every field and graph.
- Use the numbered page links at the bottom to move between pages.
- **Sort** menu: **Last updated**, **First updated**, **Titles (A-Z)**, **Titles (Z-A)**, **Templates**. The results refresh after you choose one.
- The **Date** switch shows or hides the last modification dates.

### Downloading results

1. Tick the checkbox of each record you want, or click **Select All** to select every record matching your search (across all pages). Untick a record to exclude it. While anything is selected, the button reads **Download (<number>)**. **Select All** turns into **Select None**. Selections are remembered when you change page. The **Download** button is greyed out while nothing is selected.
2. Click **Download**.
3. In the **Download Data** box ("Choose a download format:") choose one of:
   - **Simple Export (.xlsx)** (selected by default)
   - **Simple Export (.csv)**
   - **AsphaltMine Format (.xlsx)**. The box notes: "AsphaltMine Format is compatible with AsphaltMine upload, but takes much longer." For thousands of records this can take tens of minutes.
4. Click **Download** (or **Cancel**).
5. A loading indicator appears while the file is prepared. The file then downloads automatically. If something goes wrong you see "File generation failed", "Error fetching download status" or "Download failed".

The Database page offers Excel and CSV downloads. To download a single record as XML, open it in Data Curation and click **Download** (section 3).

**Downloading everything you can see at once:** open the Database page, leave the search box blank so every record you may see is listed, click **Select All** (it selects every matching record across all pages), then click **Download** and choose a format. You get all records that your account is allowed to see, not records that are private to other users. Very large downloads take longer to prepare, and the **AsphaltMine Format (.xlsx)** option is the slowest.

The Database page requires you to be logged in. If you are not, you are sent to the login page first and then returned to the Database page.

## 6. My Data, Shared Workspaces, My Profile and File Attachments

### My Data

My Data lists the records you own. The heading shows the number of records.

**Finding records.** The filter bar has:

- A search box ("Search records"),
- A workspace dropdown (**All workspaces**, **No workspace**, or a particular workspace),
- A test dropdown (**All tests** or a particular test),
- A funnel button (tooltip "Filter") to apply,
- **Clear all**, which resets the filters.

**Download Data** (top right): downloads all your records. A **Download Data** box offers the same three formats as the Database page (Simple Export (.xlsx), Simple Export (.csv), AsphaltMine Format (.xlsx)). If you have no records you see "No Data to download."

**The table** shows **Name**, **Test**, **Last Modification date**, **Workspace** ("None" if not in a workspace) and **Actions**. Click the sliders icon in **Actions** for one record:

- **View**: opens the record in Data Curation.
- **Edit**: opens the record in edit mode in Data Curation (section 3). Greyed out if you may not edit it.
- **Change workspace**: opens a box "Select a new workspace to assign the record". Choose **No workspace** or one of the workspaces you can write to, then click **Change**. If you have no workspace with write access, a message says you do not have access to any workspace with sufficient rights.
- **Change Owner**: opens a box "The owner of the record(s) will be modified. Please select the new owner:". Choose a user (any active user other than yourself) and click **Change**. Only the owner can use it (greyed out otherwise).
- **Delete**: asks "Are you sure you want to delete the record ?" Click **Yes** to delete or **No** to cancel. Only the owner can use it (greyed out otherwise). Deleting cannot be undone.

**Acting on many records at once**: click **Modify Records**. Checkboxes appear, and the button changes to **Done**. Tick records, or tick the checkbox in the table header to select every record matching the current filters, on all pages. A counter shows "<n> records selected". Then open **Choose action** (disabled until at least one record is selected) and pick:

- **Delete selected records**
- **Change owner of selected records**
- **Move selected records to a workspace**

Click **Done** to leave this mode and clear the selection.

**Making records public or private.** There is no public or private switch on individual records. Visibility is controlled by workspaces:

- A record in **No workspace** is visible only to its owner.
- A record placed in a workspace is visible to the people who have access to that workspace.
- If a workspace is marked public (marked "(public)" in workspace lists), its records are visible to everyone. AsphaltMine may also provide a global public workspace. If one appears in your list of workspaces, moving a record there makes it public.
- To share or publish a record, use **Change workspace** (or **Move selected records to a workspace**) to move it into the right workspace. To make it private again, choose **No workspace**.

### Shared Workspaces

Shared Workspaces lists the workspaces you own, and those in which you were given read or write access. The page heading reads "My workspaces" with a count.

**Creating a workspace**: click **Create workspace**, type a name in **Workspace name** in the "Create new workspace" box, then click **Create Workspace** (or **Cancel**). This needs write access; read-only accounts cannot create a workspace. There is no limit on how many workspaces a user with write access can create.

**The table** has: **Title**, **Records** (how many), **Owner**, **Can read**, **Can write**, **Public** (shown as Yes or No), and **Actions**. Click a row (or **View Content**) to open the workspace.

**Actions** menu for a workspace:

- **View Content**: opens the workspace contents.
- The following are offered only to the workspace owner:
  - **Rename**: type a **New title** and click **Rename**.
  - **Manage Access**: decide who can see or edit the workspace (see below).
  - **Set public** or **Set private**: makes the workspace, and so its records, visible to everyone, or restricts it again. A box asks "Are you sure you want to set the workspace public?" (or private). Not offered for the global workspace, and only offered if the website allows setting workspaces public.
  - **Delete**: removes the workspace. Offered only when the workspace is not public.

**Managing access to a workspace** (owner only):

1. Open **Actions** on the workspace and click **Manage Access**. The page reads "Edit access to workspace: <name>" and shows a **Public** badge if it is public.
2. Click **Add users** and search by name in the "Search users..." box to add people as chips. Tick **Write access** if they should also be able to add or edit records. The box explains: "Selected users can always view this workspace. Enable write access to also let them add or edit records." Click **Add**.
3. Click **Add groups** to do the same for groups.
4. In the **Users** and **Groups** tables, the **Write access** switch toggles write rights for each entry, and **Remove** takes the access away (you are asked to confirm).
5. Click **Previous page** to go back.

For a public workspace, the tables list only the users and groups with write access.

**Opening a workspace**: the workspace page shows its name at the top and two tabs, **Data (<number>)** and **Files (<number>)**. **Download Data** downloads the workspace records in the same three formats. **Previous page** goes back. Records in a workspace have the same **Actions** menu as in My Data (View, Edit, Change workspace, Change Owner, Delete), with entries greyed out when you lack the rights. If the workspace is empty the page says "The collection is empty." If you have no read right you see an "Access Forbidden" message.

### My Profile

Open **My Account** and click **My Profile**. The page shows your name and username, and three buttons:

- **Preferences**: choose your **Time zone** from a list and click **Set**. Dates on the website are shown in that zone.
- **Edit Profile**: change **First Name**, **Last Name** and **Email Address**, then click **Save changes** (or **Cancel**). A message "Profile information edited." confirms it.
- **Change Password**: enter your old password and your new password twice, following the password rules, and click **Save changes**. Not shown when the website uses single sign-on.

Below the buttons the page lists **Username**, **Email**, **Write Access**, **Admin**, **Last Login** and **Date Joined**.

If **Write Access** is No, a **Request Write Access** button sits next to it. Clicking it opens a form asking for **Organization name** (Institute, company or university), **Country or countries** (source of data), the **standards followed for the data** (European standards, or Other with a field to specify which), and a short **Description** of why you need write access. Click **Send Request** to submit it to the AsphaltMine team, or **Cancel** to close it. Once sent, the button is replaced by a **Request sent** label. When the team accepts the request, an email confirms that your account now has write access and recommends organizing your data into workspaces. If they deny it, you keep read-only access and can send a new request.

### File Attachments

Open **My Account** and click **File Attachments**. The heading reads "My files". It lists files you have uploaded to AsphaltMine.

- Click **Upload File**, choose a file under "Choose file to upload:", and click **Upload** (or **Cancel**).
- The table shows **File name**, **Upload date**, **Workspace** ("None" if not in a workspace) and **Actions**.
- **Actions** menu: **View**, **Download**, **Share PID** (greyed out unless available), **Change workspace**, **Change Owner** and **Delete**. Some entries are greyed out when you lack the rights.

Files can also be viewed on the **Files** tab of a workspace. Files are separate from test records.

## 7. Visualization

Visualization can be opened without logging in. It has two tabs at the top: **General** and **Live Insights**. Live Insights is selected when the page opens.

### General

The **General** tab shows a welcome text ("Welcome to the AsphaltMine Visualization Dashboard") and notes that the dashboard is continuously updated.

### Live Insights

Live Insights shows live summaries of the curated records in the database. A **Live** badge and an "Updated ..." time (for example "Updated just now" or "Updated 5 min ago") show when the numbers were last refreshed. Click **Refresh** to recalculate the numbers now. With the **All Data** scope, **Refresh** recalculates the numbers for you only, so a record you just saved shows up immediately in your view, while other users keep seeing the shared numbers until the next automatic update, which happens every hour for everyone. You can refresh once a minute, and you must be logged in to do it. If you are not logged in the **Refresh** button is greyed out with the tip "Sign in to refresh", and for a minute after each refresh it is greyed out and shows a countdown such as "Refresh (42s)". While it refreshes, the numbers on screen stay in place and are replaced when the new ones are ready. For a **Workspaces** scope the numbers are always calculated live from your own workspaces.

**Choosing what to summarize (scope).**

- **All Data** (default): summarizes all curated records in the database. Only summary numbers and charts are shown, never the records themselves.
- **Workspaces**: summarizes only records in workspaces you choose. It is locked (greyed out, with the tip "Sign in to filter by workspace") if you are not logged in.

To use **Workspaces**:

1. Click **Workspaces**.
2. Click the "Search workspaces…" box, type part of a name, and click a workspace to add it as a chip. You can add several. Public workspaces are marked "(Public)". Only workspaces you can read or write are listed. Click the cross on a chip to remove it.
3. Until you pick one, the page says "No workspace selected." If nothing is found you see "No records found for the selected workspace(s)."
4. After you pick a workspace, three extra filters appear: search boxes for **mix types**, **years** and **binder grades**. Type in a box, click a value to add it as a chip, and remove it with its cross. The buttons **Clear mix types**, **Clear years** and **Clear binder grades** reset each one. **Clear all** removes the workspace chips and the extra filters.

Changing the scope or filters clears the selected test in the "By Test" part of the page and reloads everything.

**Overview charts (always shown for the current scope).**

- A **Total Records** tile.
- **Record Distribution by Test** (bar chart) with the record count.
- **Mixing Method** (pie chart).
- **Target Binder Grade** (bar chart of the most reported grades).
- **Records by Year** (line chart).
- Summary cards for **Binder Content (%)**, **RAP Content (%)**, **Maximum Density (Mg/m³)**, **Recovered Penetration (0.1mm)**, **Recovered Softening Point (°C)** and **Recovered Elastic Recovery (%)**. Each card shows the average, a bar marking the 95% interval (the range that covers most of the values, with low and high ends), and the number of records behind it. If nothing has been reported for a field the card says "No data reported for this field in the current scope."
- **Sieve Gradation Composition (as designed)** and **Sieve Gradation Recovered Materials**: a line for the mean percent passing at each sieve size, with a shaded band for the 95% interval. Hover over a point to see details.

**Expanding distributions and exporting.**

- Click a summary card to open its **Distribution** (a histogram of the values) in a larger window. Click any chart to enlarge it in the same way.
- Every chart has a small toolbar with three buttons: **Expand**, **Save as PNG** (saves the picture) and **Export as CSV** (saves the numbers).
- Click the small information icon next to a chart title for a definition of the quantity.

**By Test (drill-down).**

1. Under **By Test**, click one of the test buttons: **Marshall**, **ITS**, **Rutting**, **Stiffness**, **TSRST** or **UTST**. Until you pick one the page says "No test selected."
2. The page then shows, for that test only:
   - **Mixture Insights**: the same mixture charts and cards as above, limited to records of that test, with the record count.
   - **Test Results**: summary cards for that test's key results, each with average, 95% interval and record count. For example, Marshall shows Stability, Flow, Marshall Quotient, Bulk Density, Air Voids, VMA and VFB; ITS shows Test Temperature, ITSR, ITS Dry and ITS Wet; Rutting shows Test Temperature and Mean Proportional Rut Depth; TSRST shows start temperature, temperature rate, failure stress and failure temperature; UTST shows test temperature, deformation rate, tensile strength and failure strain; Stiffness shows stiffness modulus.
   - **Correlation Analysis**: a matrix showing how strongly pairs of parameters relate. The lower triangle uses the Pearson coefficient (linear relation) and the upper triangle uses the Spearman coefficient (rank based relation). Each cell shows the coefficient and, beneath it, the number of paired records. Cells with too few paired records say "not enough records". Click a cell to open a scatter plot of the two parameters. Use **Show more parameters** or **Show fewer parameters** below the matrix to add or hide extra parameters.
3. If a test has no records in the current scope the page says "No records found for this test in the current scope."

If the data cannot be loaded you see messages such as "Could not load data for this scope."

## 8. Prediction

Prediction can be opened without logging in. It uses trained models to estimate results from mixture properties without running the test. The page has three tabs: **General**, **Performance Prediction** and **Mix Design**.

- **General**: a welcome text ("Welcome to the AsphaltMine Prediction Dashboard"). New models are added over time.
- **Mix Design**: currently says "To be added...".
- **Performance Prediction**: contains a row of model buttons: **Rutting Test**, **Marshall Test**, **ITS**, **TSRST**, **Stiffness Test** and **Volumetric Properties**.

### What is available today

- **Marshall Test**: predicts Marshall Stability (kN) and Marshall Flow (mm).
- **Volumetric Properties**: predicts Bulk Density (Mg/m³) and Air Voids (%) of the compacted mixture.
- **Rutting Test**, **ITS**, **TSRST** and **Stiffness Test**: not available yet. Each shows "Performance Prediction: To be added..."

### Running a Marshall prediction

The Marshall page says "Input your parameters to predict Marshall Stability and Flow" and notes that the parameters are for materials recovered from the mixtures. Every field is required.

1. Open **Performance Prediction**, then **Marshall Test**.
2. Optional: click **Assumptions & Conditions** to read the model scope (the test standard, the training data and its limits). The **Random Fill** button fills the form with example values inside typical ranges, and **Clear** empties the form and results.
3. Under **Volumetric Properties**, enter **Maximum Density** (Mg/m³) and **Bulk Density** (Mg/m³). Bulk Density must be lower than Maximum Density.
4. Under **Binder Properties**, enter **Penetration** (0.1mm) and **Softening Point** (°C) of the recovered binder.
5. Under **Composition**, enter **Binder Content** (%) and the **Gradation**: the percentage passing each sieve size, from 0.063 mm up to 45 mm (0.063, 0.125, 0.25, 0.5, 1, 2, 4, 5.6, 8, 11.2, 16, 22.4, 31.5 and 45 mm). Values are percentages from 0 to 100, and each value must be at least as large as the one for the next smaller sieve.
6. Click **Predict**. A "Predicting, please wait..." message shows while it runs.

Hover over or click the information icon next to a field name to see an explanation and example.

### Running a Volumetric Properties prediction

1. Open **Performance Prediction**, then **Volumetric Properties**.
2. Enter **RAP Content** (%), **Maximum Density** (Mg/m³), **Binder Content** (%) and the **Gradation** as percent passing at 0.063, 0.5, 1, 2, 4, 8, 11.2 and 22.4 mm.
3. Click **Predict**.

Random Fill, Clear and Assumptions & Conditions work as on the Marshall page.

### Results

- A **Mixture Properties** picture shows your gradation curve and mixture properties.
- **Prediction Results**:
  - Marshall: a plot of Marshall Stability against Flow, and intervals for each result under **Marshall Stability Intervals** and **Marshall Flow Intervals**, shown as ±σR and ±R ranges. A note gives the experimental reproducibility defined by EN 12697-34.
  - Volumetric: the predicted **Bulk Density** and **Air Voids**, each with a ±σR range. Air Voids is calculated from the predicted bulk density and the Maximum Density you entered.
- Click **Download PDF Report** below the results to save them as a PDF.

### Input errors

If something is wrong you see a **Validation Errors** box with messages such as:

- "Bulk Density must be less than Maximum Density."
- "Percentage passing Sieve <size> (<value>%) must be greater than percentage passing <smaller size> (<value>%)". This means the gradation values must not decrease as the sieve size gets bigger.
- Browser tooltips such as "Enter a valid positive number." or "Enter a valid number between 0 and 100." if a number is missing or badly formatted.

Fix the entries and click **Predict** again.

### Limits of the models

- The Marshall model was trained on 2656 records, all from Switzerland (Canton Zurich and Canton Aargau), mostly asphalt concrete. About 70 percent used polymer modified binders (mainly grades 45/80-80 and 45/80-65, all SBS modified) and about 30 percent used unmodified binders (mainly 50/70 and 70/100). Marshall tests were run at 60°C, following EN 12697-34. It was built with Physics-Informed Neural Networks, and the paper describing it is cited in the Assumptions & Conditions window. The density of binder is fixed at 1.02 Mg/m³ (prior to October 2026 it was 1.03 Mg/m³), and the Assumptions & Conditions window lists this as the last of the Model Boundary Conditions.
- The Volumetric Properties model is an Artificial Neural Network. Inputs are limited to RAP content, binder content, maximum density and gradation. Predictions outside the range of the training data may be less reliable.
- Treat predictions for materials that differ strongly from these training conditions with caution.

## 9. Help and FAQ

Click **FAQ** in the footer at the bottom of any page. A row of category pills at the top of the page (Getting Started, Accounts & Access, Data Curation, Bulk Upload, Database & Search, My Data & Workspaces, My Profile, Visualization, Prediction, Ask AsphaltMine, Publications & Contact) jumps straight to that section. Click a question to open or close its answer. By default the questions are:

**Getting Started**
- **What is the AsphaltMine?** A platform that collects asphalt test results in an organized online database and uses the data to train machine learning models that predict asphalt performance.
- **What tasks can I perform on the AsphaltMine?** Input and curate asphalt test results, search and explore existing data, display or conceal your data, and share it publicly or with specific groups.
- **What asphalt tests are available in the AsphaltMine?** Rutting Test, Marshall Test, Indirect Tensile Strength Test, Thermal Stress Restrained Specimen Test (TSRST), Uniaxial Tension Stress Test (UTST) and Stiffness Test.
- **Do I need an account to use the AsphaltMine?** Visualization, Prediction and the FAQ open without an account. Searching the database, entering and uploading data and workspaces need a login.

**Accounts & Access**
- **How do I get access to the AsphaltMine?** Create an account with **Log In / Sign Up** then **Create Account**, and verify the email. The account is then active with read-only access; write access is a separate, optional step requested from My Profile.
- **How do I create an account?** See section 2, Signing up.
- **I did not receive the verification email. What can I do?** Check spam, then use the resend option (section 2, Resending the verification email).
- **I forgot my password. How do I reset it?** See section 2, Forgot password and password reset.
- **What can I do with a read-only account?** Log in, search and view records, and use Visualization and Prediction. Saving records needs write access, requested with the Request Write Access button on the My Profile page.
- **How do I request write access?** Open My Account, then My Profile, click Request Write Access, fill in the form, and click Send Request. You will get an email once the team decides.
- **What happens after I send a write access request?** Accepted: an email confirms write access was granted. Denied: you keep read-only access and can send a new request.

**Data Curation**
- **How do I enter a new test record?** See section 3.
- **Can I enter results for more than one test at once?** Yes, tick several tests in Select Performance Tests; one record is saved per test.
- **Why can't I save my record?** A required field is empty or invalid, or your account lacks write access ("Insufficient Permission.").
- **How do I edit a record I already saved?** Open it from Database or My Data (owner only), change it, click Update then Confirm.
- **What does "semi-mandatory" mean for a field?** The form allows saving without it, but the record isn't complete without at least one entry of grain size distribution, binder content, penetration, and voids (section 3 lists the exact pairs).
- **How do I download a single record as a file?** Open it in Data Curation and click Download; it saves as XML.

**Bulk Upload**
- **How do I upload many records at once?** Download the template, fill it in, upload it, then Extract, Validate, Save in order.
- **Where do I get the Excel template?** The "here" link on Bulk Upload, or download an existing record as AsphaltMine Format (.xlsx).
- **Is there a file size limit for Bulk Upload?** About 10 MB; split larger files.
- **What does "INVALID: Missing field" mean?** A required value is empty in that row/column; fill it in and re-upload.
- **Can one row create more than one record?** Yes, one record per test that has results in that row.

**Database & Search**
- **How do I search for records?** Type a keyword and press Enter or the space bar to turn it into a tag; a record must match all of your keywords. Click the magnifying glass button or wait three seconds to run the search.
- **What download formats are available?** Simple Export (.xlsx), Simple Export (.csv), AsphaltMine Format (.xlsx, Bulk Upload compatible but much slower, tens of minutes for thousands of records).
- **How do I download every record I can see?** Leave the search box blank, Select All, then Download.

**My Data & Workspaces**
- **Who can see the data I upload?** Private to you by default; visible to others only if moved into a shared or public workspace.
- **How do I create a workspace?** Shared Workspaces, Create workspace, name it, Create Workspace. Needs write access; read-only accounts cannot create a workspace.
- **Can I give someone write access without making my workspace public?** Yes, as owner: Manage Access, add the user/group, tick Write access for that entry.
- **How do I move several records into a workspace at once?** My Data, Modify Records, tick records, Move selected records to a workspace.
- **Can I change who owns a record?** Yes, if you own it: Actions, Change Owner, pick another active user.

**My Profile**
- **How do I change my password?** My Account, My Profile, Change Password (not shown with single sign-on).
- **How do I change my time zone?** My Account, My Profile, Preferences, choose zone, Set.

**Visualization**
- **What is Live Insights?** Live summaries of curated records (or chosen workspaces), auto-updated hourly or manually via Refresh (once a minute, logged in only).
- **Can I see statistics for just my own workspace?** Yes, switch scope to Workspaces and pick one or more.
- **What is the correlation matrix?** In a test's drill-down: Pearson coefficient below the diagonal, Spearman above, with paired-record counts.

**Prediction**
- **Which predictions are available?** Marshall Test (stability and flow) and Volumetric Properties (bulk density and air voids). Other tests will be added over time.
- **How accurate is the Marshall prediction model?** Physics-Informed Neural Networks trained on 2656 Swiss records, results shown with ±σR/±R intervals per EN 12697-34.
- **What data was the Marshall model trained on?** 2656 Swiss records (Zurich, Aargau), ~70% polymer modified binders, tested at 60°C.
- **Can I download my prediction results?** Yes, Download PDF Report below the results.

**Ask AsphaltMine**
- **What is Ask AsphaltMine?** The chat button at the bottom right of the pages: this AI assistant.
- **Does the assistant remember my earlier questions?** Only within the same browser tab, roughly the last 8 exchanges; cleared by the refresh icon or closing the tab.

**Publications & Contact**
- **Where can I find AsphaltMine's published papers?** Publications page says "Coming soon." The Marshall paper is already published (DOI 10.1016/j.cscm.2026.e05829).
- **How do I contact the AsphaltMine team for questions?** Write to contact@asphaltmine.org.

Data Curation and Bulk Upload each also have a **Quick Start** button that opens a short step by step guide.

# AsphaltMine Test Data Field Glossary

This section explains what each field means in AsphaltMine's six test data types. Fields that are identical in several tests are listed once under the tests that share them. Use it to answer questions such as what a field means or what a test records.

## Fields shared by all six tests

### DataSourceType

- **MeasurementCampaignID**: Denotes a unique alpha-numeric identifier (key) for a measurement campaign within the organization reporting the data. It is formatted as an alpha-numeric string.
- **OrganizationName**: Name of the organization where the data were reported (Company, Institute, Laboratory, etc).
- **LocationCountry**: Indicates the country where the work was performed and/or the location of the corresponding organization.
- **Year**: Year when the work referenced by the data was completed.
- **Notes**: The content of the text note concerning the data source.

### DataRecordType
Record information about the document in which the data are reported. This feature variable is structured and has two possible mutually exclusive values: "CompleteDataRecord" or "DOIdentifier".

- **DOIdentifier**: The DOI code assigned to the document in which the data are reported, serving as the sole bibliographic information.

### ArticleInJournaleType

- **FirstAuthor**: The full name of the first author of the journal article in which the data are reported.
- **Co-Authors**: The full name of a co-author of the journal article in which the data are reported. Multiple instances can be generated to include more than one co-author.
- **ArticleTitle**: The title of the journal article in which the data are reported.
- **JournalTitle**: The title of the journal in which the article reporting the data was published.
- **JournalVolumeNumber**: The volume number of the journal where the article reporting the data was published.
- **JournalIssueNumber**: The issue number of the journal where the article reporting the data was published.
- **ArticleStartingPage**: The starting page of the article in which the data are reported.
- **ArticleEndingPage**: The ending page of the article in which the data are reported.
- **ArticleNumber**: The article number in the journal in which the data are reported, applicable if the corresponding journal uses article numbers instead of pages.
- **Year**: The year when the article was published in print form.
- **Publisher**: The name of the publisher of the journal in which the article reporting the data was published.
- **DOI**: The DOI code assigned to the journal article in which the data are reported.
- **ISSN**: The International Standard Serial Number of the journal in which the article reporting the data was published.

### ArticleInConferenceProceedingsType

- **FirstAuthor**: The full name of the first author of the proceedings article in which the data are reported.
- **Co-Authors**: The full name of a co-author of the conference proceedings article in which the data are reported. Multiple instances can be generated to include more than one co-author.
- **ArticleTitle**: The title of the conference proceedings article in which the data is reported.
- **ConferenceTitle**: The title of the conference in which the article reporting the data was presented.
- **ConferenceCity**: The name of the city where the conference was held.
- **ConferenceCountry**: The name of the country where the conference was held.
- **ConferenceProceedingsTitle**: The title of the conference proceedings in which the article reporting the data was published.
- **ConferenceProceedingsVolumeNumber**: The number of the volume of the conference proceedings if available.
- **ConferenceProceedingsStartingPage**: The starting page of the conference proceedings article in which the data are reported.
- **ConferenceProceedingsEndingPage**: The ending page of the conference proceedings article in which the data are reported.
- **Year**: The year when the conference proceedings article was published in print form.
- **Publisher**: The name of the publisher of the conference proceedings in which the article reporting the data was published.
- **DOI**: The DOI code assigned to the conference proceedings article in which the data are reported.

### BookPublicationType

- **FirstAuthor**: The full name of the first author of the book (or book chapter) in which the data are reported.
- **Co-Authors**: The full name of a co-author of the book (or book chapter) in which the data are reported. Multiple instances can be generated to include more than one co-author.
- **BookTitle**: The title of the book in which the data are reported.
- **BookChapterTitle**: The title of the chapter of the book in which the data are reported.
- **ChapterNumber**: The number of the chapter of the book in which the data are reported.
- **Editors**: The name of the Editors of the book, if the case applies.
- **EditionNumber**: The edition number of the book in which the chapter reporting the data was published.
- **ChapterStartingPage**: The starting page of the book chapter in which the data are reported.
- **ChapterEndingPage**: The ending page of the book chapter in which the data are reported.
- **Year**: The year when the conference proceedings article was published in print form.
- **Publisher**: The name of the publisher of the book in which the chapter reporting the data was published.
- **DOI**: The DOI code assigned to the book chapter in which the data are reported.
- **ISBN**: The International Standard Book Number of the book in which the data are reported.

### PublishedReportType

- **FirstAuthor**: The full name of the first author of the published report in which the data are reported.
- **Co-Authors**: The full name of a co-author of the published report in which the data are reported. Multiple instances can be generated to include more than one co-author.
- **ReportTitle**: The title of the published report in which the data are reported.
- **ReportNumber**: The alphanumeric identifier of the published report in which the data are reported.
- **Year**: The year when the published report reporting the data was published in print or digital form, depending on the case.
- **Publisher**: The name of the publisher or Organization that published the report in which the data are reported.
- **DOI**: The DOI code assigned to the publsihed report in which the data are reported.
- **URL**: The Uniform Resource Locator of the published report.

### UnPublishedReportType

- **FirstAuthor**: The full name of the first author of the unpublished report in which the data are reported.
- **Co-Authors**: The full name of a co-author of the unpublished report in which the data are reported. Multiple instances can be generated to include more than one co-author.
- **ReportTitle**: The title of the unpublished report in which the data are reported.
- **Year**: The year when the unpublished report reporting the data was first available in print or digital form, depending on the case.
- **URL**: The Uniform Resource Locator of the unpublished report.

### OtherRecordsType

- **Information**: Information describing the data source.

### MixtureType

- **Notes**: The content of the text note concerning the mixture.

### MixtureIdentifiersType
The identifiers for the mixture, binder, and the laboratory reporting document

- **MixtureID**: The local identifier used for the mixture.
- **MixtureType**: The mixture type.

### MixtureRecipeType
The mixture component materials and their proportions as planned in the recipe.

- **Composition**: The percentage by mass of the components of the bituminous mixture.
- **MixtureMaximumDensity**: The value of the maximum density of the bituminous specimen, expressed in Mg/m^3 (e.g., 2.48).

### CompositionType

- **AggregatesDistribution**: The distribution of grain sizes by mass for the aggregates.
- **VirginFiller**: The percentage by mass of the virgin filler to the total mass of the bituminous mixture.
- **RecoveredFiller**: The percentage by mass of the recovered filler to the total mass of the bituminous mixture.
- **ReclaimedAsphalt**: The percentage by mass of the reclaimed asphalt to the total mass of the bituminous mixture.

### MixtureComponentPropertiesType

- **PreMixingBinderBlend**: The properties of the binder blend that contains the virgin binder, the reclaimed binder and the additives.

### AggregateType

- **GrainSizeDistribution**: The distribution of grain sizes by mass for the aggregates.
- **Nature**: The nature of the aggregates in the bituminous mixture.
- **LosAngelesTestResult**: The percentage of wear calculated during the Los Angeles Abrasion Test according to EN 1097-2, expressed as a percentage of the original weight of the sample.
- **FlakinessIndex**: The flakiness index of aggregates, expressed as a percentage, which is measured according to EN 933-3.
- **ShapeIndex**: The shape index of aggregates according to EN 933-4, expressed as a percentage.
- **FlowCoefficient**: The value of the flow coefficient of the aggregate according to EN 933-6, expressed in seconds.
- **NordicAbrasionValue**: The value of the Nordic abrasion according to EN 1097-9, expressed in percentage.
- **RoundedAndCrushed**: The percentage of semi-crushed, totally crushed, semi-rounded and totally rounded aggregate particles according to EN 933-5.
- **BitumenCoverageDegree**: The average proportion of the surface area of the aggregate particles that are covered with bitumen according to EN 12697-11.

### FillerType

- **Nature**: The nature of the filler in the bituminous mixture.
- **StiffeningEffect**: The value of the stiffening effect of filler aggregate when mixed with bitumen, measured in Degrees Celsius, according to EN 13179-1.
- **ParticleDensity**: The value of the particle density of the filler according to EN 1097-7, expressed in Mg/m^3.
- **WaterSusceptibility**: The value of the water susceptibility of fillers for bituminous mixtures, expressed in percentage, according to EN 1744-4.

### BinderType

- **Penetration**: The measured penetration of a standard needle at 25 Degrees Celsius according to EN 1426, expressed in tenths of a millimeter.
- **SofteningPoint**: The temperature at which the binder begins to soften and lose its rigidity according to EN 1427, measured in Degrees Celsius.
- **BTSV**: The results of the Binder Fast Characterization Test (BTSV) according to EN 17643.
- **MSCRT**: The results of the Multiple Stress Creep and Recovery Test (MSCRT) according to EN 16659.
- **FraassBreakingPoint**: The value of the Fraass breaking point according to EN 12593, at which a film of bituminous binder of a specified and uniform thickness will break under defined loading conditions, measured in Degrees Celsius.
- **AgingResistance**: The results of the Rolling Thin Film Oven Test (RTFOT) according to EN 12607-1.
- **ElasticRecovery**: The value of the elastic recovery of the binder according to EN 13398 at 25 Degrees Celsius, expressed as a percentage.
- **CohesionEnergy**: The value of cohesion energy of the bitumen obtained from the force ductility method according to EN 13589 at 5 Degrees Celsius, measured in joules per square centimetres.
- **Solubility**: The value of the percentage of mass of the soluble material to the total mass according to EN 12592.

### ReclaimedAsphaltType

- **GrainSizeDistribution**: The distribution of grain sizes by mass for the reclaimed aggregates.
- **Nature**: The nature of the aggregates in the bituminous mixture.
- **LosAngelesTestResult**: The percentage of wear calculated during the Los Angeles Abrasion Test, expressed as a percentage of the original weight of the sample. It is used to assess the hardness or resistance of aggregates to fragmentation.
- **FlakinessIndex**: The flakiness index of the reclaimed aggregates, expressed as a percentage, which is used to assess their angularity and particle shape.
- **ShapeIndex**: The shape index of the reclaimed aggregates according to EN 933-4, expressed as a percentage.
- **FlowCoefficient**: The value of the flow coefficient of the reclaimed aggregate according to EN 933-6, expressed in seconds.
- **NordicAbrasionValue**: The value of the Nordic abrasion according to EN 1097-9, expressed in percentage.
- **RoundedAndCrushed**: The percentage of semi-crushed, totally crushed, semi-rounded and totally rounded reclaimed aggregate particles according to EN 933-5.
- **BitumenCoverageDegree**: The average proportion of the surface area of the reclaimed aggregate particles that are covered with bitumen according to EN 12697-11.

### OtherComponentType

- **Name**: The name of the non-standard mixture component added to the bituminous mixture.

### AdditiveType

- **Type**: The type of the additive.
- **PercentageMass**: The percentage by mass of this additive to the total mass of the bituminous mixture.

### AdditionalPropertiesType
The name, value, and unit of measurement for any additional properties of the used material.

- **Property**: The name of the additional property of the considered raw material.
- **Value**: The value of the additional property of the considered raw material.
- **Unit**: The unit of measurement of the additional property of the considered raw material.

### MixingType

- **MixingMethod**: The name of the mixing method used, which could be laboratory hand mixing, laboratory mechanical mixing, or plant mixing.
- **TypeofMixer**: The type of the mechanical mixer used.
- **MixingSequence**: The mixing sequence followed during the mixing process of the bituminous mixture.
- **MixtureTemperature**: The value of the mixture temperature in Degrees Celsius.
- **ReclaimedAsphaltTemperature**: The temperature at which the reclaimed asphalt was heated before mixing, measured in Degrees Celsius.
- **MixingDuration**: The duration of mixing in minutes.

### OtherMixingPropertyType
The name, value, and unit of measurement for any other non-standard property in the mixing design process.

- **Name**: The name of a non-standard property in the mixing design process.
- **Value**: The value of the non-standard property in the mixing design process.
- **Unit**: The unit of measurement for the non-standard property in the mixing design process.

### RecoveredMaterialsType
The properties of the materials after recovering from the mixture.

- **Aggregates**: The properties of the recovered aggregates.
- **Binder**: The properties of the recovered binder.

### CoringType

- **PavingDate**: The date the pavement from which the sample was cored was paved."
- **CoringDate**: The date when the specimen was cored from the pavement.
- **CoringLocation**: The location where the specimen was cored from the pavement.

### MixtureAgingType

- **LooseMixture**: The aging of loose mixture according to Method A in EN 12697-52.
- **CompactedSpecimen**: The aging of compacted specimens from bituminous mixtures according to Method B in EN 12697-52.

### BulkDensityType
The value and method of measurement for the bulk density of the specimen according to EN 12697-6.

- **Value**: The value of the bulk density of the bituminous specimen.
- **MethodofMeasurement**: The method of measurement of the bulk density of the bituminous specimen.

### VoidsType
The percentage of voids in the bituminous sample.

- **AirVoids**: The percentage of air voids in the bituminous sample.
- **MineralAggregateVoids**: The percentage of voids in the mineral aggregate (VMA) in the bituminous sample.
- **VoidsFilledWithBitumen**: The percentage of voids filled with bitumen in the bituminous sample.

## Fields shared by the Rutting and Stiffness and TSRST and UTST tests

### CompactionType

- **CompactionDate**: The date of the compaction of the specimen.
- **CompactionTemperature**: The temperature at which the specimen is compacted, measured in Degrees Celsius.

## Fields shared by the ITS and Marshall tests

### CompactionPropertiesType

- **CompactionTemperature**: The temperature at which the specimen is compacted, measured in Degrees Celsius.
- **BlowsNumber**: The number of blows per side.

## Fields specific to the ITS test

### ITSExperiment

- **Notes**: Text note concerning the experiment in general.

### ITSTestResultsType

- **ITSSampleProperties**: The properties of the sample used in the ITS test.
- **ITSResults**: The results of the ITS test.
- **Notes**: The content of the text note concerning the test setup and results.

### ITSSamplePropertiesType

- **StorageConditions**: The storage conditions under which the sample was kept.

### ITSResultsType
The results of the indirect tensile strength test based on EN 12697-23.

- **TestTemperature**: The temperature at which the test was conducted, measured in Degrees Celsius.
- **IndirectTensileStrengthRatio**: The ratio of the indirect tensile strength of the wet specimens to that of dry specimens using Method A in EN 12697-12, expressed in percent.

### SampleDimensionsType
The dimensions of the considered cylindrical sample, including its height and diameter.

- **Height**: The height of the sample in mm.
- **Diameter**: The diameter of the sample in mm.

## Fields specific to the Marshall test

### MarshallExperiment

- **Notes**: The content of the text note concerning the experiment in general.

### MarshallTestResultsType

- **MarshallSampleProperties**: The properties of the sample used in the Marshall test, according to EN 12697-34.
- **MarshallResults**: The results of the Marshall test.
- **Notes**: The content of the text note concerning the test setup and results.

### MarshallSamplePropertiesType

- **StorageConditions**: The storage conditions under which the sample was kept.

### MarshallResultsType
The results of the Marshall test based on EN 12697-34:2020.

- **Stability**: The maximum load, expressed in kilonewtons kN.
- **Flow**: The deformation in millimetres (mm), at maximum load minus the nominal deformation obtained by extrapolation of the tangent of the graph of load against deformation back to zero load, according to EN 12697-34.
- **TangentialFlow**: The nominal deformation, expressed in mm. It is obtained by extrapolation of the tangent of the graph of the load as a function of the deformation in continuation up to the stability load, minus the nominal deformation obtained by extrapolating the tangent back to the zero load, according to EN 12697-34.
- **TotalFlow**: The deformation at maximum load, expressed in mm.
- **MarshallQuotient**: The ratio of the stability to the flow, expressed in kilonewtons kN per millimetres mm.
- **BulkDensity**: The mass per unit volume, including air voids, of the test specimen at a specified test temperature, prior to testing and after compaction.

## Fields specific to the Rutting test

### RuttingExperiment

- **Notes**: The content of the text note concerning the experiment in general.

### RuttingTestResultsType

- **SampleProperties**: The properties of the sample used in the rutting test.
- **Results**: The results of the Rutting test.
- **Notes**: The content of the text note concerning the test setup and results.

### SamplePropertiesType

- **StorageConditions**: The storage conditions under which the sample was kept.

### ResultsType

- **TestTemperature**: The temperature at which the test was conducted, measured in Degrees Celsius.

## Fields specific to the Stiffness test

### StiffnessTestExperiment

- **Notes**: The content of the text note concerning the experiment in general.

### StiffnessTestResultsType

- **StiffnessSampleProperties**: The properties of the sample used in the Stiffness Test.
- **StiffnessResults**: The results of the Stiffness Test.
- **Notes**: The content of the text note concerning the test setup and results.

### StiffnessSamplePropertiesType

- **StorageConditions**: The storage conditions under which the sample was kept.

### StiffnessResultsType
The results of the Stiffness Test based on EN 12697-26.

- **TestType**: The test applied to determine the stiffness according to EN 12697-26. The available choices are "2PB-TR", "2PB-PR", "3PB-PR", "4PB-PR", "IT-CY", "CIT-CY", "DTC-CY", "DT-CY" or "DT-PR".
- **BulkDensity**: The mass per unit volume, including air voids, of the test specimen at a specified test temperature, prior to testing and after compaction.

## Fields specific to the TSRST test

### TSRSTExperiment

- **Notes**: The content of the text note concerning the experiment in general.

### TSRSTestResultsType

- **TSRSTSampleProperties**: The properties of the sample used in the TSRST.
- **TSRSTResults**: The results of the TSRST.
- **Notes**: The content of the text note concerning the test setup and results.

### TSRSTSamplePropertiesType

- **StorageConditions**: The storage conditions under which the sample was kept.

### TSRSTResultsType
The results of the TSRST based on EN 12697-46.

- **StartTemperature**: The starting temperature of the test, measured in Degrees Celsius.
- **TemperatureRate**: The rate of change of the temperature throughtout the test, measured in Degrees Celsius per hour.
- **FailureStress**: The cryogenic stress that causes a failure of the specimen in the TSRST according to EN 12697-46, measured in Megapascal.
- **FailureTemperature**: The temperature at which the cryogenic stress causes a failure of the specimen in the TSRST according to EN 12697-46, measured in Degrees Celsius.
- **BulkDensity**: The mass per unit volume, including air voids, of the test specimen at a specified test temperature, prior to testing and after compaction.

## Fields specific to the UTST test

### UTSTExperiment

- **Notes**: The content of the text note concerning the experiment in general.

### UTSTestResultsType

- **UTSTSampleProperties**: The properties of the sample used in the UTST.
- **UTSTResults**: The results of the UTST.
- **Notes**: The content of the text note concerning the test setup and results.

### UTSTSamplePropertiesType

- **StorageConditions**: The storage conditions under which the sample was kept.

### UTSTResultsType
The results of the UTST based on EN 12697-46.

- **TestTemperature**: The temperature at which the test was conducted, measured in Degrees Celsius.
- **AppliedDeformationRate**: The applied deformation rate throughtout the test, expressed in percentage per minutes.
- **TensileStrength**: The maximum tensile stress measured in the UTST according to EN 12697-46, expressed in Megapascal.
- **FailureStrain**: The tensile strain measured when the tensile strength has been reached according to EN 12697-46, expressed in percentage.
- **BulkDensity**: The mass per unit volume, including air voids, of the test specimen at a specified test temperature, prior to testing and after compaction and cutting.
