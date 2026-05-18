# MARC2RDA Project Phase I Deliverables
[Phase I Landing Page](https://marc2rda.info/wiki/doku.php?id=start)
## Project Summary
This is an independent, volunteer-based project which was initiated in 2021 at the University of Washington Libraries' Cataloging and Metadata Services Department. Our project’s purpose is to create an open source transformation tool based on a robust mapping between the MARC21 Bibliographic format and the LRM/RDA/RDF ontology. <br> <br>

This project builds on the work of the RDA/MARC 21 Alignment Task Force within the RSC Technical Working Group, specifically their RDA-to-MARC mapping. <br> <br>

Phase I of the MARC2RDA Project set out to map and convert MARC21 Bibliographic fields considered core in the PCC Bibliographic Standard Record (BSR) for single-expression manifestations and simple augmentation aggregate manifestations. This phase concluded on September 30, 2025. The second phase of the project is set to begin in November 2025 and will cover resource types not included in Phase I, data provenance data, and the MARC21 Bibliographic fields considered core in the PCC CONSER Standard Record (CSR).

## [GitHub Repository](https://github.com/crystalyragui/MARC2RDA/)
### Mapping between MARC21 Bibliographic (for Phase I resource types) and LRM/RDA/RDF
* [Mapping spreadsheets in the form of a set of .csv files](https://github.com/crystalyragui/MARC2RDA/tree/main/Phase%20I%20Deliverables/Phase%20I%20Mapping%20Spreadsheets)
* [List of MARC21 fields and subfields excluded from the mapping in .csv format](https://github.com/crystalyragui/MARC2RDA/blob/main/Phase%20I%20Deliverables/Not%20Mapped.csv)
* [Approved URIs table](https://github.com/crystalyragui/MARC2RDA/blob/main/Phase%20I%20Deliverables/Approved%20URIs.csv)
### Transformation Code 
* [XSLT stylesheets](https://github.com/crystalyragui/MARC2RDA/tree/main/Working%20Documents/transformationCode) containing transformation code based on mapping spreadsheets and additional tables
* Instructions for running the transformation code, including brief guidelines for pre- and post-processing data
### Phase I Documentation
* Decisions Indexes detailing the Project's choices regarding:
    * [Mapping & Transformation](https://github.com/crystalyragui/MARC2RDA/wiki/Decisions-Index:-Mapping-&-Transformation), and
    * [Workflows](https://github.com/crystalyragui/MARC2RDA/wiki/Decisions-Index:-Workflow)
* [A comprehensive write-up of Phase I](https://github.com/crystalyragui/MARC2RDA/blob/main/Phase%20I%20Deliverables/Phase%20I%20Write-Up.pdf)
* [Background document on the Project's approach to mapping and transforming subject and classification data](https://github.com/crystalyragui/MARC2RDA/blob/main/Phase%20I%20Deliverables/Phase%201%20output_%20Transforming%20subject%20data%20from%20MARC%2021%20to%20RDA.pdf)

### Transformed MARC21 Bibliographic Records Output as LRM/RDA/RDF, including:
* Subsets of records from the Library of Congress, University of Washington Libraries, and National Library of New Zealand
    * The full set of transformed records is available as a [triplestore]([http://marc2rda.info:7200/](https://marc2rda.info/repository/)
        * [About the MARC2RDA Triplestore](https://marc2rda.info/wiki/doku.php?id=about-the-marc2rda-triplestore)
* A [web-based transformation tool](https://marc2rda.info/x/m2r-online.html) for use with small sets of test records, which does not require users to download or run the full XSLT transform on their own
    * [About the MARC2RDA Transformation Online](https://marc2rda.info/wiki/doku.php?id=about-the-marc2rda-transformation-online)
    * [About MARC2RDA Transformation in RIMMF6](https://marc2rda.info/wiki/doku.php?id=about-the-marc2rda-transformation-code-in-rimmf6)

### Feedback
* Feedback from the Project will be sent directly to the PCC and RSC

## Community Feedback
* We welcome the community to provide feedback using the [“Community Feedback Template”](https://github.com/crystalyragui/MARC2RDA/issues/new?template=community-feedback-template.md) to create issues in the Project GitHub Repository. To see feedback provided to the Project by yourself and others, [click here](https://github.com/crystalyragui/MARC2RDA/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Community%20Feedback%22).
* If you do not have a GitHub account but would like to submit feedback to the project, please feel free to fill out [this form](https://forms.gle/E9mKuV5DxKbM8MsV6).

## Join Us!
We are actively recruiting participants for Phase II of the MARC2RDA Project. We are particularly looking for folks with expertise in:

* Writing SPARQL queries
* GraphDB display
* XSLT
* Wikibase Cloud

## About Phase II
Phase II of the MARC2RDA Project will start in November 2025. This phase will expand the project’s scope to include complex aggregates, serial and other diachronic works, collection works, data provenance data, and MARC21 Bibliographic fields considered core in the PCC CONSER Standard Record (CSR). <br> <br>

If you would like to contribute to the project, please email Crystal Yragui at crystalyragui@gmail.com.
