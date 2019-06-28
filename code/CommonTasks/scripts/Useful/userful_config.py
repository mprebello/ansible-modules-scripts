failcolor='#ff3300'
okcolor='#ebfafa'
partialcolor='#ffb84d'
nonecolor='#ffff4d'

rules_validate_color = []
rules_validate_color.append([ 'Status', '^Failed$', failcolor ])
rules_validate_color.append([ 'Status', '^OK$', okcolor ])
rules_validate_color.append([ 'Status', '^Parcial$', partialcolor ])
rules_validate_color.append([ 'Status', '^None$', nonecolor ])
rules_validate_color.append([ 'Status', '^Failed$', nonecolor ])
