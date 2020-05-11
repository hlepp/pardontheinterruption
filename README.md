# Pardon the Interruption
## Author: 

Haley Lepp

Computational Linguistics 

University of Washington


## Description:
This study presents a corpus of exchanges between speakers in U.S. Supreme Court Oral Arguments. Each exchange is labeled on a spectrum of “cooperative" to “competitive" by a human annotator with legal experience in the United States. Details on the collection of these annotations can be found[here](https://digital.lib.washington.edu/researchworks/handle/1773/45514). 

## Instructions:

### Audio:
Download the appropriate oral argument recordings from https://www.supremecourt.gov/oral_arguments/argument_audio/2019
Run the audio splicing script using the time-stamp document and the appropriate recording as arguments.

`split_files.sh`

### Text:
Transcripts without timestamps are listed publicly on the website of the [U.S. Supreme Court](https://www.supremecourt.gov/oral_arguments/argument_transcript/2019)
This study made use of timestamps extracted from HTML in recordings that have been time-alined by the [Oyez Project](https://www.oyez.org/cases/2019). 
To extract the text by turns:
1. Click on the oral argument recording on the left of the page, which will bring up an animated transcript. 
1.Right click the animation and click "Inspect Element." 
1.Right click on the section marked "class="transcript-section ng-scope"" and select "copy element." This will copy all relevant HTML to the clipboard, and you can save it to a separate document. 
1.Run `extract_turns.sh`to split the transcripts into separate turns.



### Labels:
Each turn was labeled twice by unique annotators. 

Raw are saved in `annotations.txt`. The id is the numeric count of the turn in each hearing, the name of the first speaker, the name of the second speaker, and the name of the corpus concatenated with underscores. The columns "r1" and "r2" are the ratings for that clip, and the columns "a1" and "a2" are the ids of individual annotators. The demographic information for those annotators is saved in the file `demographics.txt`.

Labels are raw, as given directly by annotators. For our experiments we binned the labels into quintiles, which capture the peaks in the distribution of reviews and correlate with the set-up of the annotation software that annotators used to label the clips. We used the average label of the two annotators.

![Distribution of Labels](/images/distribution.png)

![Slider which Annotators Used for Labeling](/images/slider.png)

### Features:
Features can be extracted as relevant to individual studies. We had most success with OpenSmile feature-sets.
