# Phase II Mapping Instructions for Mapping Elements Tables
_Last updated: July 31, 2026_ <br>
## Table Links
* [Mapping expression elements.20251121](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?usp=sharing&ouid=100554980581177083034&rtpof=true&sd=true)  
* [Mapping work elements.20260415](https://docs.google.com/spreadsheets/d/1ppXyiLLIsFHboPtAqWXOTXNzLuQ_PeIH/edit?usp=sharing&ouid=100554980581177083034&rtpof=true&sd=true)
## Table Format
* These tables represent part of the workflow for Phase II mapping work for the M2R project  
* “Element assignment” and “All \[\] Elements” tabs reflect comprehensive lists of all RDA elements associated with a corresponding RDA class (entity), such as work, expression, or manifestation  
* Remaining tabs break elements down into categories based on type as follows (note: not all tables have all the below categories):  
  * Attributes  
  * Appellations (Relationships to Nomens)  
  * Relationships to Places  
  * Relationships to Timespans  
  * Relationships to Agents  
  * Relationships between Works, Expressions, Manifestations, and Items (WEMI)  
  * Primary (WEMI stack) Relationships  
  * Relationships to RDA Entities  
  * Relationships to skos:Concepts  
  * Special Relationships  
  * High-level relationships  
* By filling out the tabs in an element mapping spreadsheet, mappers set the stage for a coordinated approach to revise M2R Phase I mappings with the full scope of complexity added by aggregate and diachronic works  
* Tables are created class-by-class. Create the Expression table first, then the Work table, then Manifestation, then Item  
* Many other tables are linked from here–these are not meant to stand alone  
* *Italics indicate soft-deprecated elements*  
* Numerical subfields are handled in a standardized way and are not included here
### Tabs
* \[RDA Class\] Attributes \- Working Tab: All attribute properties with the domain of the RDA class described by the table. An attribute is “An element that is an inherent or externally imputed characteristic of an RDA entity”.  
* \[RDA Class\]-Nomen (appellations) \- Working Tab: Properties with the range of Nomen used as appellations of a given RDA class  
* \[RDA Class\]-Place \- Working Tab: Properties with the range Place for a given RDA class  
* \[RDA Class\]-Timespan \- Working Tab: Properties with the range Place for a given RDA class  
* \[RDA Class\]-Agent \- Properties with the range Agent for a given RDA class. This list is for reference only, and does not need work. See agent relators tables instead.  
* \[RDA WEMI Class\]-\[RDA WEMI Class\] \- Properties with the range \[WEMI stack class\] for a given \[WEMI stack class\]. These lists are for reference only, and do not need work. See [Headings Mapping Table]([https://docs.google.com/spreadsheets/d/1k-ZevqjVntyqyGZ89IGma5j71ySLYZabGrn4Ls5GM3E/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1k-ZevqjVntyqyGZ89IGma5j71ySLYZabGrn4Ls5GM3E/edit?usp=sharing)) instead.  
* \[RDA Class\]-Primary Relationships \- Properties which represent the connections between the Works, Expressions, Manifestations, and Items described in a given MARC record. This list is for reference only, and does not need work. These relationships are hard coded in our XSL transformation.  
* \[RDA Class\]-Special Relationships \- Working Tab: Properties which represent relationships between two separate WEMI stack classes which are not identified as primary relationships  
* \[RDA Class\]-High-Level Relationships \- Working Tab: Properties exemplifying the “Related \[RDA Class\] of \[RDA Class\]” pattern for a given RDA Class  
* \[RDA Class\]-SKOS Relationships \- Working Tab: Properties which represent relationships between a given RDA class and a skos:Concept value.  
* \[RDA Class\]-RDA Entity \- Properties which represent relationships between a given class and the super-class, “RDA Entity”. These lists are for reference only, and do not need work.  
* All \[RDA Class\] Elements \- A list of every property associated with a given RDA Class in the RDA Registry. These lists are for reference only, and should not be used or changed.  
* RDA Vocabs \- RDA vocabulary terms and associated lists to be used with RDA elements in creating FMV tables  
* RDA Vocabs (deprecated) \- RDA vocabulary terms which are deprecated. Consult during construction of FMV tables
### Columns for Working Tabs
* **RDA Element Label:** Element RDA Toolkit labels are listed and linked to corresponding element pages in the Official RDA Toolkit 
* **RDA curie:** Lists URI curies for each element and links to elements in the RDA Registry  
* **Datatype/Object:** In this field, mappers determine whether a datatype or object property is used by the M2R transformation. If both are used depending on conditions, record D/O. Datatype \= D. Object \= O. Datatype properties are used when expected values are typed as strings. Object properties are used when expected values are “things”, e.g. IRIs, RDA entities. If you are unsure, leave this column blank.  
* **MARC Field Documentation Page:** Provides links to MARC Bib documentation for all suggested fields/subfields/positions \* means specific RDA field  
* **Source: Searched MARC:** MARC fields, subfields/positions found via the M21 Bib Format manual and other searches  
* **Source: TK \>\> Element Reference:** Provides links to recommended "Element Reference: MARC21Bibliographic fields" \-- Do not record 500 fields  
* **Source: NLNZ R2M:** Provides links to NLNZ MARC encoding guidelines for the elements i.e., which MARC element they will use to encode an RDA element value  
* **Source: PCC:** Provides links to "MARC Coding Changes" section of PCC "Changes from Original RDA for Monographs"  
* **Source: M2R Mapping:** Provides links to Phase I mapping spreadsheets where P\# was found.  
* **Source: M2R coding:** Provides links to transformation coding folder(s) where P\#s were found  
* **Approved MARC:** MARC data source that has been approved after review of all source options  
* **RDA Vocab:** The RDA value vocabulary to be used as a value for an element, linked to the RDA Registry. If no vocabulary exists there, record “n/a”.  
* **FM table (needed; not needed; link to table):** Provides links to "Finding and mapping–Vocabulary" (FMV) and “Finding and Mapping–Non-Vocabulary” (FMNV) tables for RDA elements when an element has a related RDA vocabulary or is being pulled in a consistent manner from several MARC sources  
* **Example files:** Links to MARCXML files which exemplify an element mapping. Files should be saved [here](https://github.com/crystalyragui/MARC2RDA/tree/main/Working%20Documents/transformationCode/test_datasets)  
* **Status:** Indicates where a row is in the Phase II mapping workflow. Drop-down options mirror Phase II mapping project phases.  
* **Qualifier:** Ignore this column, it's part of deduplication workflow and may be deleted.
* **Notes:** Free text field to note questions and observations. Best practice is to end each note with –\[initials\], \[date in EDTF\]. Separate notes with “ ; “. Keep these brief and relevant. Do not have conversations in notes–-use GitHub instead.  
* **GitHub Issue or Discussion Links:** Links to relevant GitHub issues/discussions
### Phase II Mapping Workflow
1. Table Creation (Deborah)  
   1. Design a table with all elements for a given RDA Entity type, as described above  
   2. Fill out the following columns using RegistryViewer to semi-automate:  
      1. RDA Element (element Toolkit label with Official Toolkit link)  
      2. RDA curie  
2. Element Mapping Issue Creation (Crystal)  
   1. Create an issue for each element in a table, placing it in “To Do” status, Phase II milestone, “Element mapping” label  
      1. Link to element mapping table range  
      2. Link to FMV table if available  
   2. Project statuses for mapping issues:  
      1. To do  
      2. In progress  
      3. Ready for approved MARC  
      4. Approved MARC first pass  
      5. Awaiting review  
      6. Review in progress  
      7. Almost done \- waiting for decision, answer to question  
      8. Ready for FM  
      9. FM in progress  
      10. Ready for FM review  
      11. FM Review in progress  
      12. Ready for mapping spreadsheet update  
      13. Mapping spreadsheet update in progress  
      14. Ready for transform issue evaluation  
      15. Transform issue evaluation in progress  
      16. Done  
3. Element mapping table completion  
   1. Step 1: Complete the following columns (Ebe-Deborah, or anyone)  
      1. MARC Field Documentation Page (Deborah, or anyone)  
         1) If these links are absent, please add them in subsequent steps\!  
      2. Source: Searched MARC (Deborah)  
      3. Source: TK \>\> Element Reference (Deborah)  
      4. Source: NLNZ R2M (Ebe)  
      5. Source: PCC (Deborah)  
      6. RDA Vocab (Based on [Deborah’s table for elements and vocabs](https://docs.google.com/spreadsheets/d/1YKOFuwdt6ie9NZ9O7VZYF0JyZL5Z-QJo/edit?usp=sharing&ouid=106066247188335830400&rtpof=true&sd=true))  
   2. Step 2: **Source: M2R Mapping** (Mapping team)  
      1. Self-assign the element in the corresponding GitHub issue:  
         1) Locate an element to map by filtering open issues by label “Element mapping” and assignees “No assignees”. Self-assign the issue  
         2) Change the “Status” of the issue and corresponding element mapping table rows to “In progress”  
         3) Add a comment or edit the issue description to indicate the portion of the workflow you have taken on  
      2. Complete the Source: M2R Mapping column *for every row corresponding to the same RDA Element*  
         1) Include MARC field and subfield/character position from the existing Phase I M2R mapping spreadsheets. Link to a specific range in the spreadsheets where possible. If this is not possible, link to the relevant mapping spreadsheet  
            1) How to search for an element in the Phase I mapping spreadsheets:  
               1) Navigate to the [Google Drive](https://drive.google.com/drive/folders/0AADaSAA_Nl-vUk9PVA)  
               2) Type the P number from the RDA element curie (e.g., P10347)  into the “Search this Drive” box and press enter  
               3) Under “Search results”, select the filter drop-down for “Type” and select “Spreadsheets”  
               4) Open each spreadsheet with a name that corresponds to a MARC field and find where the element is mapped  
               5) If the element is mapped in a single row or a specific range of rows, highlight the row or range, right-click, and select “Get link to this range/row”. If not, click “Share” in the upper right corner of the spreadsheet and copy the link to the entire sheet  
               6) Insert this link into your value for the M2R mapping column
               7) Remember to look in each tab. If the element is mapped in a "deleted" tab, use your judgment on whether or not to record in the mapping elements spreadsheet. This mapping was not used for Phase I and may not be viable.
         2) Multiple values \= multiple rows. Add new rows as necessary.  
         3) Non-mapped values:  
            1) (not done) \- this mapping is planned and exists in the draft spreadsheet, but has not yet been completed (Status is Phase II)  
            2) Not found \- this mapping does not exist in the draft spreadsheet (MARC tag-element pairing)  
            3) (in Delete) \- mapping was located in a “delete” column, meaning the mapping was not included in code. These mappings are not automatically included but considered on a case-by-case basis  
            4) Not mapped \- it was decided not to map this element from this MARC field/subfield/character position, and is not planned  
            5) Not mappable \- this mapping won’t work  
            6) *Values outside this syntax should go in other columns or notes*  
         4) Change element status: “Ready for approved MARC”  
         5) **Mapping team: Complete this column for every element in a table before starting subsequent steps. It must be completed before subsequent columns can be filled out.**  
   3. Step 3: Approved MARC \- first pass (Mapping team members)  
      1. Search for elements with the status “Ready for approved MARC”  
      2. Self-assign the GitHub issue if you are not already assigned from doing a previous step:  
         1) Locate an element by filtering open issues by label “Ready for approved MARC”   
         2) Self-assign the issue  
         3) Change the “Status” of the issue and corresponding mapping element spreadsheet row(s) to “Approved MARC first pass”
         4) In the issue description, add the status and your name, so that project team members can easily see who has worked on what for that issue e.g. “Approved MARC First pass: Deborah"
      3. Review historical columns in all rows corresponding to the element you are mapping  
      4. If useful, fill out the example files column with any examples you consulted; consult examples if provided  
         1) Examples should live in [this folder](https://drive.google.com/drive/folders/1WWruth0hYEz9kEu5HhWnUaSz111PUlsn?usp=drive_link)  
      5. Review linked Source: M2R Mapping spreadsheet(s)  
      6. Decide whether the mapping is approved and record:  
         1) Element, subfield, character position (if approved), or,   
         2) n/a (not approved)  
      7. Change status to “Awaiting review”  
      8. *Repeat for each row corresponding to a given RDA element before assigning "Awaiting review" and moving to the next element*  
   4. Step 4: Review (Group)  
      1. Three days before meetings, identify a few (determine number by trial and error) elements with status “Awaiting review” and put them on the meeting agenda. Add examples. (Crystal)  
      2. Check the work in Approved MARC and discuss if needed  
      3. If further examples are needed, add to the example files column with any examples you consulted  
         1) Examples live in [this folder](https://drive.google.com/drive/folders/1WWruth0hYEz9kEu5HhWnUaSz111PUlsn?usp=drive_link)  
      4. Complete the Datatype / Object column  
         1) Is this going to map to a string (datatype: D) or thing (object: O) value, or both?  
      5. If questions/disagreement arise, discuss  
         1) If agreement is reached, make any discussed changes to Approved MARC and change status to “Reviewed”  
         2) If disagreement or questions are unresolved, discuss asynchronously for a week and put it back on the following week’s agenda  
         3) If disagreement remains, do an asynchronous poll and vote  
   5. Step 5: FM/FMV evaluation (Deborah)  
      1. Vocab \= FMV table needed  
         1) In progress? Link to table and assign status “FM in progress”  
         2) Needed? Record “needed” and assign status “Ready for FM”  
      2. Review non-vocab rows:  
         1) Do mapping spreadsheets need to be replaced by a link to an FM table?  
            1) Yes: “needed” → assign status “Ready for FM”  
            2) No or completed: “not needed” → “Ready for mapping spreadsheet update”  
            3) Already in progress: link to table, assign status “FM in progress”  
   6. Step 6: FM/FMV table completion (Deborah, Doreen, Sarah?, Ebe)  
      1. Search issues with status “Ready for FM”   
      2. Self-assign relevant element issue  
      3. Change element issue status to “FM in progress”  
      4. See instructions for FM/[FMV tables](https://docs.google.com/document/d/1kb4cvFy44Ngv0gdBPyhBF7EiQ_5uQJlwezLDRjyap3o/edit?tab=t.0#bookmark=id.qbw0vkyvrw1z)  
      5. When first pass is complete (a person has created an FM/FMV table but not reviewed it), change status to “Ready for FM review”  
      6. Self-assign review for tables you did not initially create, change status to “FM review in progress”  
         1) If questions/disagreement arise, write a comment in the mapping issue for the element describing the questions  
            1) If agreement is reached, go with it and make any discussed changes to Approved MARC, and change status to “Ready for mapping spreadsheet update”  
            2) If disagreement or questions are unresolved, label the issue with “Meeting discussion needed” and assign status “Almost done–Waiting for decision/answer to question”  
      7. When complete, assign status “Ready for mapping spreadsheet update”  
   7. Step 7: Mapping spreadsheet update (Crystal or any Phase I mapper)  
      1. Self-assign issues with status “Ready for mapping spreadsheet update” and change status to “Mapping spreadsheet update in progress”  
      2. Update mapping spreadsheets so they are usable by transform team  
         1) Do not repeat information from FM tables. Rather, link to the tables  
         2) If no changes are needed, make a comment in the issue indicating this  
      3. Assign status “Ready for transform issue evaluation”   
   8. Step 8: Transform issue evaluation (Crystal, Cypress)  
      1. Self-assign issues with status “Ready for transform issue evaluation” and change status to “Transform issue evaluation in progress”   
      2. Make sure mapping steps are complete and Approved MARC/FM tables are done & reviewed  
      3. Create a transform issue for each relevant MARC-element pair  
         1) “Ready for transform” status  
         2) Link to FM table(s)  
         3) Link to mapping spreadsheet  
         4) Link to element mapping spreadsheet  
         5) Link to & from mapping issue  
      4. If no changes are needed for the transform, close the issue  
      5. Close mapping issue

