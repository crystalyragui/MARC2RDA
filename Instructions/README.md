# Phase II Mapping Instructions for Mapping Expression Categories Table
_Last updated: January 15, 2026_

## Table of Contents
* [Table Description](https://github.com/crystalyragui/MARC2RDA/blob/main/Instructions/README.md#table-description)
    * [Tabs](https://github.com/crystalyragui/MARC2RDA/blob/main/Instructions/README.md#tabs)
    * [Columns for Working Tabs](https://github.com/crystalyragui/MARC2RDA/tree/main/Instructions#columns-for-working-tabs)
    * [Abbreviations and Acronyms Glossary](https://github.com/crystalyragui/MARC2RDA/blob/main/Instructions/README.md#abbreviations-and-acronyms-glossary)
 * [Expression Table Workflow (In Stages)](https://github.com/crystalyragui/MARC2RDA/blob/main/Instructions/README.md#expression-table-workflow-in-stages)
    * [Stage 1: Table design review and workflow development](https://github.com/crystalyragui/MARC2RDA/blob/main/Instructions/README.md#stage-1-table-design-review-and-workflow-development-december-2025)
    * [Stage 2: Columns A-E](https://github.com/crystalyragui/MARC2RDA/blob/main/Instructions/README.md#stage-2-columns-a-e-up-to-marc-field-january-2025)
    * [Stage 3: Fill out M2R Mapping column](https://github.com/crystalyragui/MARC2RDA/blob/main/Instructions/README.md#stage-3-fill-out-m2r-mapping-column-january-february-2025)   

## Table Description
* [Mapping expression categories.20251121 table](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?usp=sharing&ouid=106066247188335830400&rtpof=true&sd=true)
* This table represents a workflow for beginning Phase II mapping work for the M2R project. Major tabs reflect a comprehensive list of all RDA Expression elements followed by tabs for several element categories, including attributes, appellations, expression-place relationships, expression-timespan relationships, expression-agent relationships, expression-expression relationships, primary (WEMI stack) relationships, special relationships, and high-level relationships. By methodically filling out the element category tabs in this spreadsheet, a coordinated mapping to revise Phase I mappings with the full scope of complexity added by aggregate and diachronic works will be possible. Once expression elements have been completed, coded, tested, and revised, a similar approach may be taken with properties for other RDA entities present in MARC21 records for aggregates and diachronic works. 
### Tabs
* **Element Assignment:** The purpose of this tab is to coordinate and avoid duplication of work on the rest of the spreadsheet. All RDA Expression elements are listed by their RDA curies (column D) and Toolkit labels (column E). Elements are self-assigned by mappers using a drop-down list of names in column C. Column B is a "Status" column with drop-down options to indicate which elements have not been started, which are in progress, which are held up by questions, and which elements are done. Element definitions from the RDA Toolkit are in column F. Column A indicates the specific tab location for an element and is used to point mappers to an element's corresponding working tab and to usefully group elements. Groups of elements not ready for self-assignment are hidden.  
* **Notes:** Includes lists of actions to be taken, a brief explanation of what is included in the overall spreadsheet, and definitions for expression category acronyms used throughout the document. Also includes quotes and notes from the RDA Toolkit and other authoritative sources regarading the rest of the spreadsheet.
* **RDA vocabs:** RDA vocabulary terms to be used in creating F&M tables.
* **RDA vocabs (deprecated):** RDA vocabulary terms which are deprecated. Consult during construction of F&M tables.
* **Expr Attributes:** All attribute properties with domain of expression. An attribute property has no range in the RDA Registry, and is a description of the entity in the subject position of a triple rather than a relationship between two RDA entities. Columns include "RDA Element"/label (columns A&B) with RDA Toolkit links to elements, RDA curie (column C) with links to the RDA Registry, Datatype/object (Column D), Source:MRC Field (column E), TK R2M (column F), Source: NLNZ R2M (column G), Source: M2R mapping (column H), M2R Coding Status (column I), RDA Vocab (column J), F&M table (column K), Example input files (column L), MARC Record Format (column M), SEM (column N), AMLM (column O), MPW (column P), AUGM only (column Q), AUGM + AW (column R), PARM only (column S), PARM + AW (column T), COLM only (column U), COLM + AW (column V), AMAW/RDA Label (column W), RDA curie for RepEx (column X), Datatype/Object for RepEx (column Y), CW (column Z), DW (column AA), Mapping Approach, GitHub Issue Links (column AB), Notes (column AC)
* **Expr-Nomen (apellations):** Expression properties with the range of Nomen used as appellation of expression. Columns mirror those in the Expr Attributes tab (column letters may vary but titles are consistent).
* **Expr-Timespan:** Expression properties with range of RDA Timespan. Columns mirror those in the Expr Attributes tab (column letters may vary but titles are consistent).
*  **Expr-Agent:** Expression properties with range of RDA Agent. Columns mirror those in the Expr Attributes tab (column letters may vary but titles are consistent).
*  **Expr-Expr:** Expression properties with range of RDA:Expression. Columns mirror those in the Expr Attributes tab (column letters may vary but titles are consistent).
*  **Primary relationships:** Includes expression elements linking entities from a WEMI stack together. Columns mirror those in the Expr Attributes tab (column letters may vary but titles are consistent).
*  **Special relationships:** Relationships linking to related works, aside from primary relationships. Columns mirror those in the Expr Attributes tab (column letters may vary but titles are consistent).
*  **Expr-High Level Relationships:** Related ___ of expression relationships. Columns mirror those in the Expr Attributes tab (column letters may vary but titles are consistent).
*  **All expr. elements:** A list of all elements in the RDA registry with a domain of rda:Expression. Columns include status, label, curie, datatype, object, domain, range, definition, full URI, RDA Toolkit ID

### Columns for Working Tabs
* Working tabs include [Expr Attributes](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?pli=1&gid=1282199378#gid=1282199378&range=1:87), [Expr-Nomen (appellations)](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?pli=1&gid=705421002#gid=705421002&range=1:9), [Expr-Place](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?pli=1&gid=1553122974#gid=1553122974&range=1:11), [Expr-Timespan](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?pli=1&gid=1640322178#gid=1640322178&range=1:7), [Expr-Agent](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?pli=1&gid=1327699838#gid=1327699838&range=1:302), [Expr-Expr](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?pli=1&gid=442919093#gid=442919093&range=1:144), [Primary relationships](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?pli=1&gid=2039077452#gid=2039077452&range=1:4), [Special relationships](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?pli=1&gid=337837558#gid=337837558&range=1:12), and [Expr-High Level Relationships](https://docs.google.com/spreadsheets/d/1KACL_nBqdzq60k-kJIDi5DzYhHHAo6Mw/edit?pli=1&gid=1632754536#gid=1632754536&range=1:6).
* **RDA Element:** RDA Element tabs are nested to mirror semantic hierarchies within the RDA Registry. Element Toolkit labels are listed and linked to corresponding element pages in the Official RDA Toolkit.
* **RDA curie:** RDA curies, which are appended to create canonical RDA URIs in the RDA Registry, are listed alongside their corresponding RDA Elements. Curies are linked to corresponding elements in the RDA Registry.
* **Datatype/Object:** In this field, mappers determine whether a datatype or object property is used by the M2R transformation. If both are used depending on conditions, record D/O. Datatype = D. Object = O. Datatype properties are used when expected values are typed as strings. Object properties are used when expected values are "things", e.g. IRIs, RDA entities. If you're not sure, leave this column blank.
* **Source: MRC Field:** The MARC21 tag for the field, indicators and values, character position(s) and values, and subfields and values a mapping is relevant for. Use only as many character positions/indicators/subfields/values as needed to narrow down relevant conditions. Source:MRC Field values are hyperlinked to the MARC21 Bibliographic Standard page for the corresponding MARC field.
* **TK R2M:** Toolkit RDA to MARC mappings were considered in the M2R mapping during Phase I. Ignore and hide this column for now.
* **Source: NLNZ R2M:** Relevant RDA to MARC mappings from the National Library of New Zealand. MARC21 fields, indicators, character positions, subfields, and values are included where relevant for conditions. Hyperlinks lead to relevant sections of the NLNZ MARC bibliographic encoding corresponding to a particular Official RDA element. To be used as a reference. Ebe is in charge of filling out this column.
* **Source: M2R Mapping:** MARC21 fields, indicators, character positions, subfields, and values relevant for narrowing conditions for a M2R mapping to a particular element. Distinct mappings are listed in separate rows. Values are hyperlinked to corresponding M2R mapping spreadsheets for fields, or subsets of rows within those spreadsheets if they are longer. MARC2RDA mapping team is collectively responsible for filling out this row. 
* **M2R Coding Status:** Indicates whether the mapping in the Source: M2R Mapping column has been coded by the transformation team.
* **RDA Vocab:** If the element is associated with an RDA value vocabulary, this column lists the name of the vocabulary and a link to it in the RDA Registry.
* **F&M table (needed, not needed, link to table):** This column provides links to "Finding & Mapping" tables where applicable. F&M tables are used when an element has a related RDA vocabulary or when values for an element can be found in multiple MARC fields and subfields. Where tables exist, they are named and linked in this column. Where columns are needed/not needed, that is indicated in this column.
* **Example input files:** Links to example input files for this element are included here. Locations for input file storage have not yet been identified. Ignore and hide this column for now.
* **MARC Record Format:** If a MARC2RDA mapping in a given row is only relevant for a particular MARC21 record format or list of formats, include abbreviations for those formats here. This duplicates information found in conditions listed in the Source:M2R Mapping column, which is OK. Record formats include Books (BKS), Computer Files (COMP), Continuing Resources (CR), Maps (MAP), Mixed Materials (COLL), Scores (SCO), Sound Recordings (MUS), and Visual Materials (VM)
* **SEM:** Record "X" if mapping applies to single-expression manifestations
* **AMLM:** Record "X" if mapping applies to amalgamation expressions
* **MPW:** Record "X" if mapping applies to Whole work, i.e., a work that has parts that can be described separately, but are integral to the completeness of the whole
* **AUGM only:** Record "X" if only the augmented (primary) work and expression are mapped
* **AUGM + AW:** Record "X" if both the augmented (primary) work and expression and the aggregating work are mapped
* **PARM only:** Record "X" if only the parallel work and expressions are mapped
* **PARM + AW:** Record "X" if both the parallel work and expressions and the aggregating work are mapped
* **COLM only:** Record "X" if only the collected work(s) and  expressions are mapped
* **COLM + AW:** Record "X" if both the collected work(s) and expression(s) and the aggregating work are mapped
* **AMAW/RDA Label:** Record the label for the RDA property used for the mapping when an aggregating work embodied in an augmentation aggregate manifestation is the entity being described in a given mapping when applicable.
* **RDA curie for RepEx:** When mapping to an aggregating work embodied in an aggregate manifestation, list the RDA curie for the property used and link to the RDA Registry entry for that element.
* **Datatype/Object for RepEx:** Relates to the element in the preceding "RDA curie for RepEx" column. Is a datatype or object property used, or both? Leave blank if unsure.
* **CW:** Record "X" if mapping applies to collection works (collections of items, not collections of expressions)
* **DW:** Record "X" if mapping applies to diachronic works.
* **GitHub Issue or Discussion Links:** List useful titles, discussion or issue numbers, and hyperlink to relevant GitHub issues and discussions. Separate multiple values by entering on separate lines (Ctrl+Enter in Google Sheets)
* **Notes:** Leave notes for your friends! Separate multiple values with " ; " and always leave your initials and a date in EDTF format at the end. Keep these brief and relevant. Longer-form questions and conversations belong in GitHub.

### Abbreviations and Acronyms Glossary
*  SEM: Single Expression Manifestation
*  AMLM: Amalgamation expression. A [single work is realized as an amalgamation](https://access.rdatoolkit.org/en-US_ala-4d4d3f5b-8d94-3ee5-89d8-241a98366db4/div_sql_2zm_2fb)
*  MPW: Whole work, i.e., a work that has parts that can be described separately, but are integral to the completeness of the whole
*  AUGM only: Only the Augmented (primary) work and expression are mapped
*  AUGM + AW: Both the augmented (primary) work and expression and the Aggregating work are mapped
*  PARM only: Only the parallel work and expressions are mapped
*  PARM + AW: Both the parallel work and expressions and the aggregating work are mapped
*  COLM only: Only the collected work(s) and expressions are mapped
*  COLM + AW: Both the collected work(s) and expressions(s) and the aggregating work are mapped
*  AMAW/RDA Label: The aggregating work is mapped, and the RDA label is for the property used with the aggregating work (not the expression property at the beginning of the row). 
*  DW: Diachronic work
*  CW: Collection work

## Expression Table Workflow (In Stages)
### Stage 1: Table design review and workflow development: December 2025
* Review structure, purpose, and contents of table in a group meeting, reviewing the table's purpose and functionality
* Make adjustments based on group feedback
* Develop work plan and procedures for completing mapping work. Review in a group meeting and implement feedback from mapping team
* Practice one element from each tab as a group before splitting into chunks and working individually (new mapping team members will have 1-3 sessions with Crystal to begin)
### Stage 2: Column Up to MARC Field: January 2025
* Ensure completeness of columns up to MARC Field of each tab (are all relevant elements accounted for? Check against tab 1 to make sure all excluded elements are intentional)
#### Stage 3: Fill out M2R Mapping column: January-February 2025
* Copy RDA Curie "P number". Example: rdae:P20005 = P20005
* Navigate to the [M2R Google Drive](https://drive.google.com/drive/folders/0AADaSAA_Nl-vUk9PVA)
    * Paste the P number into the search box
    * Limit search results to Type:Spreadsheets
    * Click on any result that gives a MARC field tag (e.g., "586")
    * Use <Ctrl+F> to find all instances of the P number in the spreadsheet. Ignore instances in the "deleted" or "not mapped" tabs.
    * Highlight row or range of consecutive rows for the subfield or range of subfields corresponding to the RDA element you are searching for
    * Right-click >> View more row actions >> Get link to this range
    * Enter the field, indicators, character positions, subfields, and values as needed to make conditions of a mapping clear into the MARC field tag column, and hyperlink with link to range from mapping spreadsheets
        * If a spreadsheet is provided:
            * but not 'done', add "(not done)" after linked fields/subfield/position
            * but not mapped to entity in focus (e.g., Expr or Work), add "(not mapped)" after linked field/subfield/position
            * and has a Condition, add it after linked field/subfield/position; or say "(see Note)" and add it as a note   
    * When an element is present in more than one M2R mapping, create a new row for each M2R mapping link
    * As relevant, also complete GitHub Issue or Discussion Links and Notes columns as progress is made.
        * GitHub Issue or Discussion Links: This is intended for issues or discussions related only to the RDA element or MARC field in a row. A link is also included for the general spreadsheet workflow Q&A for ease of access.
* Sometimes you will run into spreadsheets which need to be amended for reasons outside the expansion into aggregates and diachronic works. When that happens, create an issue about it in GitHub (one issue per MARC tag). If you can fix it yourself you may self-assign and fix. Other members of the mapping team may also fix such issues. If a field has already been coded, it is necessary to add the "code re-check" label once a spreadsheet has been changed. Then, coders will make any needed adjustments to the transformation code. Do not close the issue until changes have been coded and tested.
 #### Stage 4: Complete up to "SEM": February-March 2025
 * Transformation team to fill out the "M2R Coding Status" column. Work coordinated by Cypress.
 * Small task committee led by Deborah to fill out "F&M table (needed; not needed; link to table) column.
     * Decide if F&M tables are needed for each element, locating tables already in existence and adding them to the spreadsheet
     * Create F&M tables
 #### Stage 5: Phase II Columns (SEM-DW)
 * [Instructions TBD]

# Field-Specific Mapping Spreadsheet Instructions
_Last updated 27 November 2024_

## Table of Contents
 - [Spreadsheet Structure](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#spreadsheet-structure)
 - [General Rules](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#general-rules)
    - [MARC tag formatting](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#marc-tag-formatting)
    - [Condition formatting](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#condition-formatting)
 - Spreadsheet columns
   - [Status](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#status)
   - [MARCField](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marcfield)
   - [MARCFieldLabel](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marcfieldlabel)
   - [MARCInd1Label](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marcind1label)
   - [MARCInd1Value](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marcind1value)
   - [MARCInd1ValueLabel](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marcind1valuelabel)
   - [MARCInd2Label](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marcind2label)
   - [MARCInd2Value](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marcind2value)
   - [MARCInd2ValueLabel](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marcind2valuelabel)
   - [CharacterPosition](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#characterposition)
   - [CharacterPositionLabel](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#characterpositionlabel)
   - [MARCSubfield](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marcsubfield)
   - [MARCSubfieldLabel](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marcsubfieldlabel)
   - [CodeValue](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#codevalue)
   - [CodeValueLabel](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#codevaluelabel)
   - [MARCTagCondition1](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marctagcondition1)
   - [Condition1Value](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#condition1value)
   - [MARCTagCondition2](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#marctagcondition2)
   - [Condition2Value](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#condition2value)
   - [RDA Registry URI](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#rda-registry-uri)
   - [RDA Registry Label](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#rda-registry-label)
   - [Recording Method](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#recording-Method)
   - [Justification for Mapping](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#justification-for-mapping)
   - [Transformation Notes](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#transformation-notes)
   - [Problems with Mapping](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#problems-with-mapping)
   - [Notes (Uncategorized)](https://github.com/uwlib-cams/MARC2RDA/tree/master/Instructions#notes-uncategorized)

 ## Spreadsheet Structure
 ### Example of an incomplete mapping
 These rows only contain the information for a possible MARC 21 field. These rows will require mapping to an RDA property, and possibly the addition of conditions or notes. Additional rows may need to be added to articulate multiple conditions, or multiple possible RDA properties.
 
 | Status | MARCField | MARCFieldLabel | MARCInd1Label | MARCInd1Value | MARCInd1ValueLabel | MARCInd2Label | MARCInd2Value | MARCInd2ValueLabel | CharacterPosition | CharacterPositionLabel | MARCSubfield | MARCSubfieldLabel | CodeValue | CodeValueLabel | MARCTagCondition1 | Condition1Values | MARCTagCondition2 | Condition2Values | RDA Registry URI | RDA Registry Label | Recording Method | Justification for Mapping | Transformation Notes | Problems with Mapping | Notes (Uncategorized) | Milestone |
 |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
 | | 210 | ABBREVIATED TITLE (R) | Title added entry | 0 | No added entry | Type | # | Abbreviated key title | | | a | Abbreviated title (NR) | | | | | | | | | | | | | | |
 
 ### Example of a partially-complete mapping
 These rows contain mappings adapted from the [RSC Technical Working Group's RDA-to-MARC 21 mapping](http://www.rdaregistry.info/Maps/mapRDA2M21B.html). These mappings should be reviewed and edited as necessary.
 
 | Status | MARCField | MARCFieldLabel | MARCInd1Label | MARCInd1Value | MARCInd1ValueLabel | MARCInd2Label | MARCInd2Value | MARCInd2ValueLabel | CharacterPosition | CharacterPositionLabel | MARCSubfield | MARCSubfieldLabel | CodeValue | CodeValueLabel | MARCTagCondition1 | Condition1Values | MARCTagCondition2 | Condition2Values | RDA Registry URI | RDA Registry Label | Recording Method | Justification for Mapping | Transformation Notes | Problems with Mapping | Notes (Uncategorized) | Milestone |
 |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
 | | 264 | PRODUCTION, PUBLICATION, DISTRIBUTION, MANUFACTURE, AND COPYRIGHT NOTICE (R) | Sequence of statements | * | | Function of entity | 4 | Copyright notice date | | | c | Date of production, publication, distribution, manufacture, or copyright notice (R) | | | | | | | http://rdaregistry.info/Elements/m/P30007 | has copyright date | | | | | | |
 
 ### Example of a complete mapping
 These rows have been filled-out, reviewed, and marked as completed in the [project page](https://github.com/orgs/uwlib-cams/projects/12/views/1).
 
 | Status | MARCField | MARCFieldLabel | MARCInd1Label | MARCInd1Value | MARCInd1ValueLabel | MARCInd2Label | MARCInd2Value | MARCInd2ValueLabel | CharacterPosition | CharacterPositionLabel | MARCSubfield | MARCSubfieldLabel | CodeValue | CodeValueLabel | MARCTagCondition1 | Condition1Values | MARCTagCondition2 | Condition2Values | RDA Registry URI | RDA Registry Label | Recording Method | Justification for Mapping | Transformation Notes | Problems with Mapping | Notes (Uncategorized) | Milestone |
 |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
 | | 490 | SERIES STATEMENT (R) | Series tracing policy | * | | Undefined | * | | | | a, x, v | | | | | | | | http://rdaregistry.info/Elements/m/P30106 | has series statement | structured description | Chose not to use sub-properties because number of conditions is not sustainable for transformation. MARC does not have separate subfields for each element. Chose to retain MARC subfields when ISBD punctuation is absent in order to maintain structure of description. | when LDR 18 = a or i, remove marc subfields and rely on ISBD punctuation. When LDR 18=c, retain marc subfield codes to separate pieces of information | | | |
 
## General Rules
 - Always check against:
   - [MARC21 Format for Bibliographic Data](https://www.loc.gov/marc/bibliographic/) (what mapping from)
   - [RDA Registry](https://www.rdaregistry.info/) (what mapping to)
   - [Official RDA Toolkit](https://access.rdatoolkit.org/) (explains how to use RDA)
   - [Decision Index](https://github.com/uwlib-cams/MARC2RDA/wiki/Decisions-Index): this provides guidance on a variety of considerations from the [Spreadsheet](https://github.com/uwlib-cams/MARC2RDA/wiki/Decisions-Index#ia-spreadsheet) to [MARC21 Fields & Subfields Not Mapped](https://github.com/uwlib-cams/MARC2RDA/wiki/Decisions-Index#ia-spreadsheet) to the [GitHub](https://github.com/uwlib-cams/MARC2RDA/wiki/Decisions-Index#iiia-github) workflow while mapping and more
 - If not applicable, leave blank. If columns are not applicable/blank, they may be hidden while working on the spreadsheet.
 - Notes should be initialed and dated, with separate notes in the same column/row separated by ;
 - In order to achieve an accurate mapping, you may need to delete rows that don't properly translate from MARC to RDA, duplicate rows, write in conditions, include more than one RDA property, and/or combine subfields into one row if they map to a single RDA element.  
 - If many subfields need to be combined to produce a value for a single RDA element, list those separate subfields in the order they should appear using "MARCSubfield" using ", " and make a transformation note to indicate exactly what the resulting value should look like.
 - If there are new additions to [MARC21 Format for Bibliographic Data](https://www.loc.gov/marc/bibliographic/), which are indicated in red font, add them to the spreadsheet.
 - Mapping Spreadsheets that are finished should move rows with [final statuses](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#status) other than "done" to new sheets in the workbook to reduce redundancy and improve readability. E.g., move deleted rows to a new “Deleted” sheet within the workbook
 - Consistently use operators:
### Operators
| Operator | Example | Details |
|---|---|---|
| 0-9 | 0-9 | any number 0-9 |
| * | * | any valid value |
| not() | not($x) | To indicate "not present" |
| # | # | Used only with indicators, to specify that the indicator is blank |
| only() | only($a) | Used with conditions, to indicate a MARC field is limited to a single subfield |
| [is[nodeType]] | [is IRI] | Value type constraint for conditions |
| \| | special issue of\|is special issue of | OR |
### MARC tag formatting
 - 3 digit tag,
 - followed by space,
 - followed by indicators,
 - followed by either...
   - _for subfields:_
     - space, then $\[letter or number\]
   - _for character positions:_
     - /\[number\]
 #### Examples:
 - 264 #1 $c
 - 007/07
 ### Condition formatting
 #### Rules
 - 1. To express a MARCTagCondition, follow the same MARC tag formatting as specified above, BUT: Do not repeat any information already expressed by other cells in the same row. For instance, if you want to express in the example row that $i has a value of "part of work", the MARCTagCondition is simply "$i".
 - 2. To express a MARCTagCondition that only requires that a field/subfield is present, write the MARCTagCondition as in rule 1, but leave the Condition1Values blank.
 - 3. To express a MARCTAgCondition where a specified subfield is the only subfield present in the field, express as in rule 1 but inside an only() operator, like so: "only($a)"
 - 4. To specify the type of value of a MARCTagCondition, express the condition as in rule 1, and express the value as [is[nodeType]], like so: "[is IRI]" 
 - 5. To express that a MARC tag or value is not present, express as in rule 1 but include either the MARC tag or value in a not() operator, like so: "not($1)"
 - 6. It's ok to use an OR operator in either MARCTagConditions or ConditionValues. Use "|" to express these relationships, like so: "not($1|$0)"
 - 7. "()" are ignored in literal values to prevent proliferation of conditions caused by similar RDA element labels. So, "part of (work)" and "part of work" are both expressed as "part of work"
 - 8. Multiple conditions on the same row must have an "AND" relationship to one another. Additional sets of condition and condition value columns may be added to facilitate more layers of conditions. If you need to add an additional set of columns, let other participants know so all spreadsheets can remain uniform.
 - 9. Conditions with "OR" relationships to one another must be expressed in separate rows of the spreadsheet.
 #### Example
 | Status | MARCField | MARCFieldLabel | MARCInd1Label | MARCInd1Value | MARCInd1ValueLabel | MARCInd2Label | MARCInd2Value | MARCInd2ValueLabel | CharacterPosition | CharacterPositionLabel | MARCSubfield | MARCSubfieldLabel | CodeValue | CodeValueLabel | MARCTagCondition1 | Condition1Values | MARCTagCondition2 | Condition2Values | RDA Registry URI | RDA Registry Label | Recording Method | Justification for Mapping | Transformation Notes | Problems with Mapping | Notes (Uncategorized) |
 |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
 | | 700 | ADDED ENTRY--PERSONAL NAME (R) | Type of personal name entry element | * | | Type of added entry | * | | | | 0 | Authority record control number or standard number (R) | | | $i | part of work\|is part of work | | | http://rdaregistry.info/Elements/w/P10019 | is part of work | identifier\|IRI | | [entity]-->[property indicated]-->[entity2]-->[property indicating relationship between entity2 and an authority for entity 2]-->[value of $0] CEC 2022-03-01 | | |
 ## Status
| Example | Details |
|---|---|
|  | Needs human review. A blank status field indicates that this mapping hasn't been reviewed by a human since it was machine-generated. If a machine-generated mapping is analyzed by a human and determined not to need changes, do not leave Status blank. |
| not mapped | If the MARC field identified in this row should be left out of the mapping for any reason, record "not mapped". |
| first pass | Once a row has been mapped by a human, but has not yet been reviewed by someone else, record "first pass". This applies even if a machine-generated mapping is reviewed and left unchanged. |
| delete | If you are certain that an existing row should be deleted from our mapping, record "delete". |
| delete? | If you think a row should be deleted from our mapping, but are not entirely sure, record "delete?". |
| ? | If you have questions or uncertainty about a row, or you think the row needs more attention from another human, record "?". |
| loss | If the MARC being expressed is more specific than available LRM/RDA/RDF allows, record "loss". We will review, compile, and send these to RSC requesting clarification or changes to Registry.  |
| reviewed | Once a first pass has been reviewed, record "reviewed". |
| done | When a row has been accounted for in the transformation code and it's ready to be published, record "done". | 
| phase II | If the MARC field is out of scope for phase I but will be addressed in phase II, record "phase II". | 
* If a not-mapped row also contains an incorrect mapping, record "not mapped" rather than "delete".
_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## MARCField
| Example | Details |
|---|---|
| 250 | Main MARC tag. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_
 
 ## MARCFieldLabel
| Example | Details |
|---|---|
| EDITION STATEMENT (R) | Label for MARC tag. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_
 
 ## MARCInd1Label
| Example | Details |
|---|---|
| Undefined | Label for the first indicator (_not_ individual values). |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## MARCInd1Value
| Example | Details |
|---|---|
| * | Value for the first indicator. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## MARCInd1ValueLabel
| Example | Details |
|---|---|
| \[blank\] | Label for the value of the first indicator |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## MARCInd2Label
| Example | Details |
|---|---|
| Undefined | Label for the second indicator (_not_ individual values). |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## MARCInd2Value
| Example | Details |
|---|---|
| * | Value for the second indicator. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## MARCInd2ValueLabel
| Example | Details |
|---|---|
| \[blank\] | Label for individual MARC second indicator values. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## CharacterPosition
| Example | Details |
|---|---|
| 0 |  |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## CharacterPositionLabel
| Example | Details |
|---|---|
| category of material | Label for the character position in the previous column (_not_ the value) |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## MARCSubfield
| Example | Details |
|---|---|
| a | Do not include symbols; just the letter/number. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## MARCSubfieldLabel
| Example | Details |
|---|---|
| Edition statement (NR) | Label for the subfield (_not_ for individual values). |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## CodeValue
| Example | Details |
|---|---|
| c | For coded fields, such as 007, where MARC has specified the meanings, the code itself goes here. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## CodeValueLabel
| Example | Details |
|---|---|
| \[blank\] | Label for the specific code indicated in previous column. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## MARCTagCondition1
| Example | Details |
|---|---|
| 264 00 $b | Mapping often needs to specify "**If A equals A1, then A maps to B**". (B=RDA Registry URI) Sometimes multiple layers of these statements are needed to achieve sufficient specificity. **This should represent A** for the _first_ layer of conditions. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## Condition1Value
| Example | Details |
|---|---|
| University of Washington | Mapping often needs to specify "**If A equals A1, then A maps to B**". (B=RDA Registry URI) Sometimes multiple layers of these statements are needed to achieve sufficient specificity. **This should represent A1** of the _first_ layer of conditions. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## MARCTagCondition2
| Example | Details |
|---|---|
| 007/00 | Mapping often needs to specify "**If A equals A1, then A maps to B**". (B=RDA Registry URI) Sometimes multiple layers of these statements are needed to achieve sufficient specificity. This should represent **A** of the _second_ layer of conditions. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## Condition2Value
| Example | Details |
|---|---|
| m | Mapping often needs to specify "**If A equals A1, then A maps to B**". (B=RDA Registry URI) Sometimes multiple layers of these statements are needed to achieve sufficient specificity. This should represent **A1** of the _second_ layer of conditions. If more conditions are needed, add another pair of columns for "MARCTagCondition3" and "Condition3Values" and so on. Do not express multiple conditions in one column. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## RDA Registry URI
| Example | Details |
|---|---|
| <http://rdaregistry.info/Elements/m/P30107> | Full URI for the RDA Registry property the MARC maps to. Use constrained properties. If there is a one-to-many mapping, create a new row so that each row is limited to one URI. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## RDA Registry Label
| Example | Details |
|---|---|
| has edition statement | Label from the RDA Registry for the URI (for human readability). Do _not_ include quotes. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## Recording Method
| Example | Details |
|---|---|
| One of the following: unstructured description, structured description, identifier, IRI | RDA Recording Method used in the MARC data, if known and if consistent. |
* Refer to [Official RDA Toolkit](https://access.rdatoolkit.org/) > Guidance > [Recording methods](https://access-rdatoolkit-org.offcampus.lib.washington.edu/en-US_ala-a06b3aa1-d994-31b1-b961-e4ce37c1a4d3)

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## Justification for Mapping
| Example | Details |
|---|---|
| We chose this property over that property because of reasons. | Notes on why a particular mapping was chosen. Not required, but recommended when multiple choices are possible. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## Transformation Notes
| Example | Details |
|---|---|
| This property should be paired with these other ones to create multiple RDA/RDF statements that look like this: \[code example in .ttl\] | Notes on what the resulting RDA-RDF should look like. Not required. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## Problems with Mapping
| Example | Details |
|---|---|
| Looks like this field with these conditions should map to some other property. | Notes on problems with the mapping. Not required. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_

 ## Notes (Uncategorized)
| Example | Details |
|---|---|
| This field is obsolete, but exists in legacy data so we should map it. -CEC 2021-09-29; Here's another note about another thing. - CEC 2021-10-01 | All notes that do not fall under another notes category. Reasons for not mapping a row/justifications for recording "Delete" or "Not Mapped go here. |

_[Return to top.](https://github.com/uwlib-cams/MARC2RDA/tree/main/Instructions#spreadsheet-instructions)_
