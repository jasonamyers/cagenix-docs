import barrel.cooper
import os
import static

app = static.Cling(os.path.join(os.path.dirname(__file__), 'build/html'))
app = barrel.cooper.basicauth(users=[('admin@cagenix.com', 'tester')])(app)
