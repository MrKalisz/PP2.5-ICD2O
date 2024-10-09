import os.path
import sys
import PP2_4

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: Invalid Input\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['super man']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Invalid Input\n"

def test_q3_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['66']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q3()
	captured = capsys.readouterr()
	assert captured.out == "In: Invalid Input\n"

def test_q4_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['Super']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q4()
	captured = capsys.readouterr()
	assert captured.out == "In: mixed\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 0\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['help5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Invalid Input\n"

def test_q3_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['bomb']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q3()
	captured = capsys.readouterr()
	assert captured.out == "In: bomb\n"

def test_q4_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['GREETINGS']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q4()
	captured = capsys.readouterr()
	assert captured.out == "In: all uppercase\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['6']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 12\n"

def test_q2_3(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['hello']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: hello is your word\n"

def test_q3_3(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['hello']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q3()
	captured = capsys.readouterr()
	assert captured.out == "In: hello does not start and end with the same letter\n"

def test_q4_3(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['bye']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q4()
	captured = capsys.readouterr()
	assert captured.out == "In: all lowercase\n"

def test_q1_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['hello']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: Invalid Input\n"

def test_q2_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['6']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Invalid Input\n"

def test_q3_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['6']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q3()
	captured = capsys.readouterr()
	assert captured.out == "In: Invalid Input\n"

def test_q4_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['6']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q4()
	captured = capsys.readouterr()
	assert captured.out == "In: Invalid Input\n"

