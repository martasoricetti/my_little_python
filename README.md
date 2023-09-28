# my_little_python
This software is meant to:
1) process data stored in different formats (JSON and CSV) and upload them in two different databases, in particular a graph and a relational database
2) query the databases simultaneously through predefined operations

To run the software you can use the script "test_final_software.py". If you have other data with the same structure of the ones inside this folder you can use them, simply by substuting the path specified in the run script.

IMPORTANT: before launching the run script you have to download "blazegraph.jar" (https://github.com/blazegraph/database/releases/tag/BLAZEGRAPH_2_1_6_RC) and open blazegraph in your terminal, simply by typing:
<code>java -server -Xmx4g -jar blazegraph.jar (use the path to your blazegraph file)</code>.
Then you have also to substitute in the run script the value of grp_endpoint with your blazegraph endpoint + '/sprql' that you can find when you open blazegraph from your terminal.
<img width="452" alt="image" src="https://github.com/martasoricetti/my_little_python/assets/92322269/6362214c-0f0f-417a-a3d1-ec09b7a30aa7">

Create also a "publication.db" file in your ptoject folder
