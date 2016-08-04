#!/usr/bin/python
# Filename: address_book.py

import cPickle as p
import os

class Contact:
	'''Represents a contact with email and mobile info'''
	def __init__(self, email, mobile):
		'''Initialize the contact with email and mobile'''	
		self.email = email
		self.mobile = mobile

class ContactAddressBook:
	'''Represents contact address book.'''

	def __init__(self, abfile):
		'''Initializes the address book ab and address book store file.'''
		self.abfile = abfile

	def add(self):
		'''To add new contact into address book'''
		# get the dict from storage file
		f = file(self.abfile, 'r')
		ab = p.load(f)

		# input new contact in loop until int put n to name			
		while True:
			name = raw_input('Enter new contact name(input n to finish) -->')
			if name == 'n':# finish to input, print current dict for reference
				print '\nThere are %d contacts in the address-book\n' % len(ab)

				for name, contactinfo in ab.items():
					print 'Contact %s info %s, %s' % (name, contactinfo.email, contactinfo.mobile)
				break
			# input email and mobile
			email = raw_input('Enter new contact email -->')
			mobile = raw_input('Enger new contact mobile -->')
			
			# create a new instance for new contact, then add to dict
			contactinfo = Contact(email, mobile)
			ab[name] = contactinfo

		# write updated dict into file
		f = file(self.abfile, 'w')
		p.dump(ab, f)
		f.close()

	def search(self):
		''' to search specifed contace by name'''
		# get the dict from storage file
		f = file(self.abfile, 'r')
		ab = p.load(f)

		while True:
			if len(ab) == 0: # No contct
				print 'address book is empty'
				break
			else:
				name = raw_input('Enter contact name for search (input n to quit, all to display all) -->')
				if name == 'n': # to quit search
					break
				elif name == 'all': # to display all contacts
					for name, contact in ab.items():
						print 'Contact %s contact info: email %s, mobile %s' % (name, ab[name].email, ab[name].mobile)
				elif name in ab: # find out
					print '%s contact info: email %s, mobile %s '  % (name, ab[name].email, ab[name].mobile)
				else: # cannot find out
					print "\n %s is not in contact address book" % name	

	def delete(self):
		''' to delete specifed contact by name'''
		# get the dict from storage file
		f = file(self.abfile, 'r')
		ab = p.load(f)

		while True:
			if len(ab) == 0: # No contact at all
				print 'address book is empty'
				break
			else: # display all contact for reference
				for name, contact in ab.items():
						print 'All contact info: %s:  email %s, mobile %s' % (name, ab[name].email, ab[name].mobile)
			# input contact name to be deleted
			name = raw_input('Enter contact name to delete (input n to finish) -->')
			if name == 'n':
				break
			elif name in ab: # delete then display all for reference
				del ab[name]
				print 'del successful'
				for name, contact in ab.items():
					print 'After del, all contact info: %s:  email %s, mobile %s' % (name, ab[name].email, ab[name].mobile)
			else: # specifie contact is not in address book
				print 'contact is not in address book, pls. check before delete'

		# write updated dict into file
		f = file(self.abfile, 'w')
		p.dump(ab, f)
		f.close()

	def revise(self):
		''' to revise specifed contact info'''
		# get the dict from storage file
		f = file(self.abfile, 'r')
		ab = p.load(f)

		while True:
			if len(ab) == 0: # No contact at all
				print 'address book is empty'
				break
			else: # display all contact for reference
				for name, contact in ab.items():
					print 'All contact info: %s:  email %s, mobile %s' % (name, ab[name].email, ab[name].mobile)
			# input contact name to be deleted
			name = raw_input('Enter contact name to revise (input n to finish) -->')
			if name == 'n':
				break
			elif name in ab: # input new contact info for revision
				email = raw_input('Enter new contact email -->')
				mobile = raw_input('Enger new contact mobile -->')
			
				# create a new instance for new contact, then revise to dict
				contactinfo = Contact(email, mobile)
				ab[name] = contactinfo
	
				print 'revise successful'
				print 'After revision, new contact info: %s:  email %s, mobile %s' % (name, ab[name].email, ab[name].mobile)

			else: # specifie contact is not in address book
				print 'contact is not in address book, pls. check before delete'

		# write updated dict into file
		f = file(self.abfile, 'w')
		p.dump(ab, f)
		f.close()

# 'ab' is short for 'a'dress'b'ook
# 'abfile' is short for address book storage file name

ab={}
abfile = 'contact_address_book.data'

# for the first time run, write empty dict into file
if not os.path.exists(abfile):
	f = file(abfile, 'w')
	p.dump(ab,f)	
	f.close()
# create contact address book instance, then to have all operations
contact = ContactAddressBook(abfile)

while True:
	name = raw_input('''Enter menu item:
		0: Search Contact
		1: Add new Contact
		2: Delete Contact
		3: Revise Contact info
		n: Quit
			''')

	if name == 'n':# quit the program
		print '\nBye\n'
		break
	elif name == '0':
		contact.search()
	elif name == '1':
		contact.add()
	elif name == '2':
		contact.delete()
	elif name == '3':
		contact.revise()
	else:
		print 'Invalid input, enter again'

