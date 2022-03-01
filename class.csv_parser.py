import re

class csv_parser:

	# Comma, not followed by a space character.
	separator = ',(?! )'

	# TODO: implement some type of functionality for this...
	# Eventually. Maybe.
	def __init__(this):
		pass

	"""I don't know that 'escape' is the best descriptor really,
	but you get the idea: append a space character to any commas 
	within a string, as not to break the CSV separator pattern 
	design."""
	def escape(this, value):
		return re.sub(this.separator, ', ', value)

	# Create a CSV-fomatted string from a list of values.
	def pack(this, csv_data):
		# Just playing it safe...
		if isinstance(csv_data, list):
			formatted = []
			for value in csv_data:
				value = value.strip()
				if isinstance(value, int):
					formatted.append(str(value))
				else:
					formatted.append('"' + this.escape(value) + '"')
			

			return str(','.join(formatted))

		return None


	# Extract data fields from a CSV-formatted string.
	def unpack(this, csv_data):
		fields = re.split(this.separator, csv_data)

		raw_values = []
		num_fields = len(fields)

		i = 0
		while i < num_fields:
			if fields[i].isnumeric():
				raw_values.append(int(fields[i]))
			else:
				raw_values.append(fields[i].strip("\x00..\x1F" + '"'))

			i += 1

		return raw_values