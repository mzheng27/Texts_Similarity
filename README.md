# Texts_Similarity
   Use python to compare the stems, sentence length, use of punctuates in text files to judge if a piece a text is more likely to belong to some source file based on their similarity score. 

   When testing the model, my partner Yunan and I create source1, 'JKR,' from four passages by J.K.Rowling, and source2, 'NYT,' for the four passages from the New York Times. These eight passages in total set up our source bodies. 

   To set up the comparison, we uses the two left-out passages, one from J.K.Rowling, and one from the New York Times. In addition, we had a short story, called 'tale' by Minglan (this is written in poetry style, and every two consecutive lines rhym), and a news story written for CO201 class by Yunan. We wanted to compare these four passages as the new texts against with the source bodies we set up.

   The results we've got show that this program's accuracy. The NYT_leftout has higher similarity scores with NYT; JKR_leftout with JKR. The "Tale" written in short verse and old-fashion/formal tone has a higher similarity score with New York Times, so does the news story written by Yunan.



>> Below is the exact results:

scores for JKR: [-11623.777, -3571.47, -11407.804, -307.164, -953.305]
scores for NYT: [-11310.747, -3537.345, -11181.389, -312.843, -552.136]
tale is more likely to have come from NYT

scores for JKR: [-5189.194, -1560.995, -5096.503, -108.263, -567.459]
scores for NYT: [-4752.453, -1506.764, -4700.175, -105.046, -350.151]
CO 201 is more likely to have come from NYT

scores for JKR: [-25313.976, -7934.651, -24826.189, -1199.26, -1942.661]
scores for NYT: [-26893.495, -8029.362, -26623.172, -1294.503, -4002.042]
JKR_leftout is more likely to have come from JKR

scores for JKR: [-19096.045, -5727.211, -18741.56, -543.872, -1739.281]
scores for NYT: [-17209.304, -5603.489, -16913.421, -574.507, -931.699]
NYT_leftout is more likely to have come from NYT
