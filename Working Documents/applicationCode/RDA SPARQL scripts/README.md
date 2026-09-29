Preamble
--------

This folder contains code based on Gordon Dunsire's notes in the MARC2RDA Triplestore working group.
I wrote the code for each SPARQL query in perl, then 'translated' that into python.

Each script demonstrates one of Gordon's SPARQL queries against a 'live' triplestore.
This is possible using some fairly basic code--thanks to the RDF4J API.

The code is available here as: rda_sparql_examples.zip
Installation steps (for Windows): Installation.txt
General notes about the usage follow.


About the code
--------------

The 'rda_sparql_examples' folder layout is as follows:

rda_sparql_examples
    * lib	- code common to each set of scripts
    * perl	- scripts written in perl (.pl files)
    * python	- python versions of the above (.py files)
    * sparql	- a library of SPARQL queries (as .rq. files)
	
During the coding process a shared package evolved for perl
(later also 'translated' into python):
	- perl - 'uses' the RDF4J.pm module
	- python - 'imports' the m2r_rdf4j.py module

The shared package performs common tasks such as
  - setting default values (SPARQL endpoints, language code, RDA curies, etc.)
  - IRI normalization, curie expansion, string escaping, etc.
  - dispatching a query to graphDB and processing the response

In the perl and python folders, there are two scripts 
for each one of Gordon's SPARQL queries:
	1. one uses the SPARQL 'library' in the sparql folder
	2. the other includes each SPARQL query in the code itself.

Style #1 is indicated by a leading underscore in the script name.
For example:
	_get_nomen_string.py -- loads the SPARQL query from the library
	get_nomen_string.py -- codes the SPARQL query in the script itself

The following forms for RDA elements are accepted in function parameters
   rdand:P80068
   http://rdaregistry.info/Elements/n/datatype/P80068
   <http://rdaregistry.info/Elements/n/datatype/P80068>

Placeholders for parameters are given in uppercase and enclosed in double underscores:
 __IRI__
__LANGCODE__

Query functions expect IRI arguments to already be SPARQL-ready.
Thus callers should run sparql_iri() before building a query.

When coding a sparql query for a known element, prefer its IRI:
   <http://rdaregistry.info/Elements/n/datatype/P80068>

If you chose to use curies in a query, prepend a 'PREFIX' statement to the query:
   PREFIX rdand: <http://rdaregistry.info/Elements/n/datatype/>
   
The list of sparql queries coded thus far is as follows:

best_access_point_by_entity.rq
marc_source_by_entity.rq
nomen_string_by_entity.rq
registry_label_by_element.rq
toolkit_label_by_element.rq

The 'label' queries were repeated to demonstrate different forms for RDA elements.

Process
-------

Although I have been using/learning perl for many years, 
I am just learning python myself (hence the need to rely on 
agentic coding in the python scripts). 

The process used was:

- write the code in perl on ubuntu
- test it, fix problems, test it again, etc.
- once all scripts were working, revise each to follow a consistent method
- use an agent to render each perl script into python on ubuntu
- test it, fix problems, test it again, etc.
- run pylint on each script until it reaches 10/10
- copy the 'rda_sparql_examples' folders to windows
- test each stream and note what wasn't working on windows
- return to ubuntu, tweak what was needed for cross-platform compatibility
- repeat the last 3 steps until the same code was working on each platform

I haven't tried to develop a 'best practice' in these scripts;
instead I've focused on consistency and simplicity, and the
ultimate test for any code: does it do what its meant to do?

The python scripts might benefit from review by someone
who actually knows the language well :-)
