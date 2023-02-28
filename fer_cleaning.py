# Rename subfolders
old_names = ["anger", "sadness", "happiness", "fear", "surprise"]
new_names = ["angry", "sad", "happy", "fear", "surprise"]
for i, s in enumerate(old_names):
  os.rename(os.path.join(TEST_PATH,old_names[i]), os.path.join(TEST_PATH,new_names[i]))

# Remove emotions not needed
removes = ["contempt", "disgust", "neutral"]
import shutil
for i in removes:
  shutil.rmtree(os.path.join(TEST_PATH,i))