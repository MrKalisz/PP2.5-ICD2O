import os.path
import sys
import PP2_4

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "Invalid Input\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "Invalid Input\n"

def test_q3_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q3()
	captured = capsys.readouterr()
	assert captured.out == "Invalid Input\n"

def test_q4_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q4()
	captured = capsys.readouterr()
	assert captured.out == "mixed\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "0\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "Invalid Input\n"

def test_q3_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q3()
	captured = capsys.readouterr()
	assert captured.out == "bomb\n"

def test_q4_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q4()
	captured = capsys.readouterr()
	assert captured.out == "all uppercase\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "12\n"

def test_q2_3(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "hello is your word\n"

def test_q3_3(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q3()
	captured = capsys.readouterr()
	assert captured.out == "hello does not start and end with the same letter\n"

def test_q4_3(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q4()
	captured = capsys.readouterr()
	assert captured.out == "all lowercase\n"

def test_q1_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "Invalid Input\n"

def test_q2_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "Invalid Input\n"

def test_q3_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q3()
	captured = capsys.readouterr()
	assert captured.out == "Invalid Input\n"

def test_q4_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q4()
	captured = capsys.readouterr()
	assert captured.out == "Invalid Input\n"

