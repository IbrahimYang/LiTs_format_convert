# DIR 
<pre>
root
|___src
|	|___python_code
|
|___liver_database
|	|___1-input_nrrd: input nrrd dir the nrrd should be lower 1 class dir of root
|	|___2-output_volumes: output have mat,vision,label dir and 1 txt file
|	|___3-input_result: input CNN result
|	|___4-input_result_th: output 3D-crf and thresholding output
|	|___5-output_nrrd: convert input_result_th to nrrd file
|
|___data_template:A nrrd data template
<code>
