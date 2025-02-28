# cloud_ass3
# Docker Run Command to Verify Output
To ensure `result.txt` is created and persists after the container exits, please run:

docker run --rm -v $(pwd)/output:/home/data/output cloud_ass3

# How to Check the Output File
After running the above command, check the output file with:

ls -l output/
cat output/result.txt

This will ensure that the `result.txt` file is available for verification.
