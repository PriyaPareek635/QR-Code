import webbrowser

f = open('home.html','w')
message="""<!DOCTYPE html>
<html>
<head> 
	<title>Home </title>
</head>

<body>
	<center>
	<form method="get" action="F:/QR/qrcode-reader-master/index.html">
		<button type="submit"><h1>QR Code</h1></button>
	</form>
		
	</center>
   
</body>
</html>"""
f.write(message)
f.close()

webbrowser.open_new_tab('home.html')
