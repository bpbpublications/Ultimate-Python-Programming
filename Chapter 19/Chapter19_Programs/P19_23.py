L = ['names.doc', 'file2.xls', '', 'info.doc', 'help.doc', '', 'show.ppt']
print(list(filter(lambda s : s.endswith('.doc'), L)))

print(list(filter(None, L)))