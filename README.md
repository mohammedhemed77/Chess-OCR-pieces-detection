# Chess-OCR-pieces-detection

![screenshot](logo.jpg)

## steps :

(1) Download about 1M games from lichess https://database.lichess.org/standard/lichess_db_standard_rated_2014-07.pgn.zst
then i choose july 2014 as it's about 1M games, then i use python chess package to convert about 60k positions from these games , and generate about 190k position images.

(2) Create csv labels file that contains fen for each image.

(3) Annotate about 64K images and label each one of them in a taxt file with same name of the specific image and each file contains bboxes for each piece in the board.
i make function to do this task.

if you want to skip first 3 steps, don't worry you can download the annotated ready to train dataset which i uploaded to huggingface : 

(4) Train YOLO11 model on these dataset.
The model works very well, i uploaded output of the model during training in a file called run_logs you can check it 

(5) Extract images from pdf chess book , i choose one of them 

(6) Test the results on the extracted image and open lichess to analyze position and find the best move. 

note that the model sometimes get confused, it detects the black king as white king , in the case that the extracted image quality not good and may need some enhancement using openCV. 
