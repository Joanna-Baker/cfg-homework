import pytest

@pytest.mark.me
def test_read():
    """
    This methods reads the specified file. "r" stands for read.
    """
    f = open("fixtures/single_line_testfile.txt", "r")
    assert f.read() == "Hello there"


def test_readline():
    """
    This method returns one line from the specified file
    """
    f = open("fixtures/single_line_testfile.txt", "r")
    assert f.readline() == "Hello there"


def test_readlines():
    """
    This method returns a list of each line in the file
    """
    f = open("fixtures/multi_line_testfile.txt", "r")
    assert f.readlines() == ["This is a line of text\n", "This is another line of text"]



def test_write(tmpdir):
    """
    This method writes the specified text to the specified file.
    "a" stands for append and adds the lines to the end of the file,
    whereas "w" clears the file and inserts the text.
    """
    file = tmpdir.join('output.txt')
    with open(file.strpath, 'w') as fp:
        fp.write('This is a line of text\n')
    assert file.read() == 'This is a line of text\n'


def test_writelines(tmpdir):
    """
    This method writes the items of a list to the specified file.
    "a" stands for append and adds the lines to the end of the file,
    whereas "w" clears the file and inserts the text.
    """
    file = tmpdir.join('output.txt')
    with open(file.strpath, 'w') as fp:
        fp.writelines(['This is a line of text\n', 'This is another line of text'])
    assert file.readlines() == ['This is a line of text\n', 'This is another line of text']
