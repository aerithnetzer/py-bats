import os
import filecmp

from bib2md import bib2md

def test_bib2md():

    # Print a header for the test
    print("----------------------------")
    print("bib2md: Running assertions")


    # Create a temporary directory for testing
    os.mkdir("test_dir")
    os.chdir("test_dir")

    # Create a test .bib file
    with open("test.bib", "w") as f:
        f.write("@article{test,\n")
        f.write("  author={John Doe},\n")
        f.write("  title={A Test Article},\n")
        f.write("  journal={Journal of Testing},\n")
        f.write("  year={2021}\n")
        f.write("}")

    # Call the bib2md function
    bib2md()

    # Check that the .md file was created
    assert os.path.isfile("test.md")

    # Check that the .md file is not empty
    assert os.path.getsize("test.md") > 0

    # Check that the .md file has the expected content
    with open("test.md", "r") as f:
        content = f.read()
        assert "John" in content
        assert "A test article" in content
        assert "Journal of Testing" in content
        assert "2021" in content

    # If passed all assertions, then the test passed
    
    print("bib2md: All assertions passed")
    print("----------------------------")

    # Clean up the temporary directory
    os.chdir("..")
    import shutil

    shutil.rmtree("test_dir")

test_bib2md()
