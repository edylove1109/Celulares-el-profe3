from pathlib import Path

EMAIL = 'juancarlospelayolepe7' + '@' + 'gmail.com'

p = Path('app/src/main/java/com/celulareselprofe/app/MainActivity.kt')
s = p.read_text()
s = s.replace('val isAdmin = roleLower == "admin" || roleUpper == "admin"', 'val isAdmin = roleLower == "admin" || roleUpper == "admin" || user.email?.equals(EMAIL, ignoreCase = true) == true')
s = s.replace('adminRole = role1.equals("admin", ignoreCase = true) || role2.equals("admin", ignoreCase = true)', 'adminRole = role1.equals("admin", ignoreCase = true) || role2.equals("admin", ignoreCase = true) || email.equals(EMAIL, ignoreCase = true)')
s = s.replace('error.code', 'error.message')
s = s.replace('juancarlospelayolepe7@gmail.com', EMAIL)
p.write_text(s)

r = Path('firestore/firestore.rules')
if r.exists():
    t = r.read_text()
    old = "function isAdmin() {\n     return signedIn() &&\n       (get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role in ['admin', 'Admin', 'ADMIN'] ||\n        get(/databases/$(database)/documents/users/$(request.auth.uid)).data.Role in ['admin', 'Admin', 'ADMIN']);\n   }"
    new = "function isAdmin() {\n     return signedIn() &&\n       (request.auth.token.email == '" + EMAIL + "' ||\n        get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role in ['admin', 'Admin', 'ADMIN'] ||\n        get(/databases/$(database)/documents/users/$(request.auth.uid)).data.Role in ['admin', 'Admin', 'ADMIN']);\n   }"
    t = t.replace(old, new)
    r.write_text(t)
