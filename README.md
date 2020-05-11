# Pardon the Interruption

Author: Haley Lepp, University of Washington Computational Linguistics


## Description:
This study presents a corpus of exchanges between speakers in U.S. Supreme Court Oral Arguments. Each exchange is labeled on a spectrum of 0 ("very competitive") to 100 ("very cooperative") by a human annotator with legal experience in the United States. Details on the collection of these annotations can be found [here](https://digital.lib.washington.edu/researchworks/handle/1773/45514). 

Information about the audio segments and annotations included in the corpus is listed below.

|Number of oral arguments|4|
|Number of annotated segments|732|
|Number of annotators per segment|2|
|Number of unique annotators|77|
|Number of segments annotated by each annotator|1 - 26 (+ 2 “dummy” segments)|
|Number of Unique Male Participants|11 including Justice Thomas, who does not speak|
|Number of Unique Female Participants|9|
|Number of Justice to Non-Justice exchanges|338|
|Number of Non-Justice to Justice exchanges|351|
|Number of Justice to Justice exchanges|22|
|Number of Non-Justice to Non-Justice exchanges|0|
|Number of Female to Female exchanges|127|
|Number of Male to Male exchanges|269|
|Number of Female to Male exchanges|165|
|Number of Male to Female exchanges|150|

## Instructions:

### Audio:
Download the appropriate oral argument recordings from the website of the [U.S. Supreme Court](https://www.supremecourt.gov/oral_arguments/argument_audio/2019).
Run the audio splicing script using the appropriate recording as an argument.

`split_files.sh <recording>`

### Text:
Transcripts without timestamps are listed publicly on the website of the [U.S. Supreme Court](https://www.supremecourt.gov/oral_arguments/argument_transcript/2019).
This study made use of timestamps extracted from HTML in recordings that have been time-alined by the [Oyez Project](https://www.oyez.org/cases/2019). 
To extract the text by turns:
1. Click on the oral argument recording on the left of the page, which will bring up an animated transcript. 
2. Right click the animation and click "Inspect Element." 
3. Right click on the section marked "class="transcript-section ng-scope"" and select "copy element." This will copy all relevant HTML to the clipboard, and you can save it to a separate document. 
4. Run `extract_turns.sh`to split the transcripts into separate turns.



### Labels:
Each turn was labeled twice by unique annotators. 

Raw are saved in `annotations.txt`. The id is the numeric count of the turn in each hearing, the name of the first speaker, the name of the second speaker, and the name of the corpus concatenated with underscores. The columns "r1" and "r2" are the ratings for that clip, and the columns "a1" and "a2" are the ids of individual annotators. The demographic information for those annotators is saved in the file `annotator_demographics.txt`. 

Labels are raw, as given directly by annotators. For our experiments we binned the labels into quintiles, which capture the peaks in the distribution of reviews and correlate with the set-up of the annotation software that annotators used to label the clips. We used the average label of the two annotators.

Distribution of Labels

<img src="img/label_distribution.png" width="500">

Slider which Annotators Used for Labeling

<img src="img/slider.png" width="500">

### Features:
Features can be extracted as relevant to individual studies. We had most success with OpenSmile feature-sets.
