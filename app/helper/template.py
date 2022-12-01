
# template email order
def templateHTML(username, total_harga):

	html = f"""
	<!DOCTYPE html>

	<html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
	<head>
	<title></title>
	<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
	<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
	<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
	<!--[if !mso]><!-->
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Roboto+Slab" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Cabin" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Oxygen" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Droid+Serif" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Playfair+Display" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" type="text/css"/>
	<!--<![endif]-->
	<style>
	""" 

	mid = """
			* {
				box-sizing: border-box;
			}

			body {
				margin: 0;
				padding: 0;
			}

			a[x-apple-data-detectors] {
				color: inherit !important;
				text-decoration: inherit !important;
			}

			#MessageViewBody a {
				color: inherit;
				text-decoration: none;
			}

			p {
				line-height: inherit
			}

			.desktop_hide,
			.desktop_hide table {
				mso-hide: all;
				display: none;
				max-height: 0px;
				overflow: hidden;
			}

			@media (max-width:700px) {
				.desktop_hide table.icons-inner {
					display: inline-block !important;
				}

				.icons-inner {
					text-align: center;
				}

				.icons-inner td {
					margin: 0 auto;
				}

				.row-content {
					width: 100% !important;
				}

				.mobile_hide {
					display: none;
				}

				.stack .column {
					width: 100%;
					display: block;
				}

				.mobile_hide {
					min-height: 0;
					max-height: 0;
					max-width: 0;
					overflow: hidden;
					font-size: 0px;
				}

				.desktop_hide,
				.desktop_hide table {
					display: table !important;
					max-height: none !important;
				}

				.row-3 .column-1 .block-1.paragraph_block td.pad {
					padding: 5px 30px !important;
				}

				.row-2 .column-1 .block-2.heading_block td.pad {
					padding: 10px 60px 30px !important;
				}

				.row-2 .column-1 .block-2.heading_block h1 {
					font-size: 33px !important;
				}

				.row-4 .column-1 .block-1.heading_block h2,
				.row-6 .column-1 .block-1.heading_block h2 {
					font-size: 20px !important;
				}
			}
		</style>
	"""

	end = f"""
	</head>
	<body style="margin: 0; background-color: #1a30eb; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1a30eb;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1a30eb; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 20px; padding-bottom: 10px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="heading_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad" style="width:100%;text-align:center;">
	<h1 style="margin: 0; color: #ffffff; font-size: 23px; font-family: Poppins, Arial, Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: 700; letter-spacing: normal; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Fashion Campuss Email Notification</span></h1>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-size: auto;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-size: auto; background-color: #ffffff; color: #000000; border-bottom: 0 solid #FFFFFF; border-left: 0 solid #FFFFFF; border-radius: 30px 30px 0 0; border-right: 0px solid #FFFFFF; border-top: 0 solid #FFFFFF; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="heading_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:30px;padding-left:60px;padding-right:60px;padding-top:70px;text-align:center;width:100%;">
	<h1 style="margin: 0; color: #020b22; direction: ltr; font-family: Poppins, Arial, Helvetica, sans-serif; font-size: 40px; font-weight: 700; letter-spacing: normal; line-height: 150%; text-align: center; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Halo {username}!</span></h1>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 60px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="paragraph_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:5px;padding-left:60px;padding-right:60px;padding-top:5px;">
	<div style="color:#878787;direction:ltr;font-family:Poppins, Arial, Helvetica, sans-serif;font-size:16px;font-weight:400;letter-spacing:0px;line-height:120%;text-align:center;mso-line-height-alt:19.2px;">
	<p style="margin: 0;">Terimakasih Sudah berbelanja di Fashion Campuss. Berikut adalah total pembelanjaan anda :</p>
	</div>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 50px; padding-right: 50px; vertical-align: top; padding-top: 0px; padding-bottom: 40px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="heading_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:10px;padding-top:5px;text-align:center;width:100%;">
	<h2 style="margin: 0; color: #878787; direction: ltr; font-family: Poppins, Arial, Helvetica, sans-serif; font-size: 26px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Rp. {total_harga}</span></h2>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 50px; padding-right: 50px; vertical-align: top; padding-top: 40px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="text_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:15px;padding-left:30px;padding-right:30px;padding-top:10px;">
	<div style="font-family: sans-serif">
	<div class="" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #888888; line-height: 1.2; font-family: Poppins, Arial, Helvetica, sans-serif;">
	<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><strong><span style="font-size:20px;">Belanja Terus Di Website kami</span></strong></p>
	</div>
	</div>
	</td>
	</tr>
	</table>
	<table border="0" cellpadding="0" cellspacing="0" class="text_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:15px;padding-left:5px;padding-right:30px;padding-top:10px;">
	<div style="font-family: sans-serif">
	<div class="" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #888888; line-height: 1.2; font-family: Poppins, Arial, Helvetica, sans-serif;">
	<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><strong><span style="font-size:20px;">Sampai Jumpa di Orderan Berikutnya</span></strong></p>
	</div>
	</div>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-6" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f2f5ff; border-radius: 0 0 30px 30px; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 15px; padding-bottom: 15px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="heading_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:20px;padding-top:20px;text-align:center;width:100%;">
	<h2 style="margin: 0; color: #1a30eb; direction: ltr; font-family: Poppins, Arial, Helvetica, sans-serif; font-size: 20px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Fashion Campuss</span></h2>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-7" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1a30eb; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 25px; padding-bottom: 25px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="20" cellspacing="0" class="text_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
	<tr>
	<td class="pad">
	<div style="font-family: sans-serif">
	<div class="" style="font-size: 12px; font-family: Poppins, Arial, Helvetica, sans-serif; mso-line-height-alt: 18px; color: #fafafa; line-height: 1.5;">
	<p style="margin: 0; font-size: 10px; text-align: center; mso-line-height-alt: 15px;"><span style="font-size:10px;"><span style="">© 2022 Fashion Campuss. </span></span><span style="font-size:10px;"><span style=""> All Rights Reserved.</span></span></p>
	</div>
	</div>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-8" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="icons_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad" style="vertical-align: middle; color: #9d9d9d; font-family: inherit; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;">
	<table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="alignment" style="vertical-align: middle; text-align: center;">
	<!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
	<!--[if !vml]><!-->
	<table cellpadding="0" cellspacing="0" class="icons-inner" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;">
	<!--<![endif]-->
	<tr>
	<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 6px;"><a href="https://www.designedwithbee.com/" style="text-decoration: none;" target="_blank"></a></td>
	<td style="font-family: Poppins, Arial, Helvetica, sans-serif; font-size: 15px; color: #9d9d9d; vertical-align: middle; letter-spacing: undefined; text-align: center;"><a href="https://www.designedwithbee.com/" style="color: #9d9d9d; text-decoration: none;" target="_blank"></a></td>
	</tr>
	</table>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table><!-- End -->
	</body>
	</html>
	"""
	result = f'{html} {mid} {end}'
	return result

# template verify email address
def templateVerifEmail(username,uuid):
	first = f"""
	<!DOCTYPE html>

	<html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
	<head>
	<title></title>
	<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
	<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
	<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
	<!--[if !mso]><!-->
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Roboto+Slab" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Cabin" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Oxygen" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Droid+Serif" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Playfair+Display" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" type="text/css"/>
	<!--<![endif]-->
	<style>
	"""

	mid = """
			* {
				box-sizing: border-box;
			}

			body {
				margin: 0;
				padding: 0;
			}

			a[x-apple-data-detectors] {
				color: inherit !important;
				text-decoration: inherit !important;
			}

			#MessageViewBody a {
				color: inherit;
				text-decoration: none;
			}

			p {
				line-height: inherit
			}

			.desktop_hide,
			.desktop_hide table {
				mso-hide: all;
				display: none;
				max-height: 0px;
				overflow: hidden;
			}

			@media (max-width:700px) {
				.desktop_hide table.icons-inner {
					display: inline-block !important;
				}

				.icons-inner {
					text-align: center;
				}

				.icons-inner td {
					margin: 0 auto;
				}

				.row-content {
					width: 100% !important;
				}

				.mobile_hide {
					display: none;
				}

				.stack .column {
					width: 100%;
					display: block;
				}

				.mobile_hide {
					min-height: 0;
					max-height: 0;
					max-width: 0;
					overflow: hidden;
					font-size: 0px;
				}

				.desktop_hide,
				.desktop_hide table {
					display: table !important;
					max-height: none !important;
				}

				.row-3 .column-1 .block-1.paragraph_block td.pad {
					padding: 5px 30px !important;
				}

				.row-2 .column-1 .block-2.heading_block td.pad {
					padding: 10px 60px 30px !important;
				}

				.row-2 .column-1 .block-2.heading_block h1 {
					font-size: 33px !important;
				}

				.row-6 .column-1 .block-1.heading_block h2 {
					font-size: 20px !important;
				}
			}
		</style>
	"""
	end = f"""
	</head>
	<body style="margin: 0; background-color: #1a30eb; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1a30eb;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1a30eb; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 4ArnkyH51JRD2r6QNhraoYfZJ5vrwQh3dczAM6WnRm5P64CgwwDzXoffBJT7nNm1tVfDLn6UtNC7vbs39vQD6x7EU1CLaSY: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="heading_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad" style="width:100%;text-align:center;">
	<h1 style="margin: 0; color: #ffffff; font-size: 23px; font-family: Poppins, Arial, Helvetica, sans-serif; line-height: 120%; text-align: center; direction: ltr; font-weight: 700; letter-spacing: normal; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Fashion Campuss Email Notification</span></h1>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-size: auto;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-size: auto; background-color: #ffffff; color: #000000; border-bottom: 0 solid #FFFFFF; border-left: 0 solid #FFFFFF; border-radius: 30px 30px 0 0; border-right: 0px solid #FFFFFF; border-top: 0 solid #FFFFFF; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 4ArnkyH51JRD2r6QNhraoYfZJ5vrwQh3dczAM6WnRm5P64CgwwDzXoffBJT7nNm1tVfDLn6UtNC7vbs39vQD6x7EU1CLaSY0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="heading_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:30px;padding-left:60px;padding-right:60px;padding-top:70px;text-align:center;width:100%;">
	<h1 style="margin: 0; color: #020b22; direction: ltr; font-family: Poppins, Arial, Helvetica, sans-serif; font-size: 40px; font-weight: 700; letter-spacing: normal; line-height: 150%; text-align: center; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Halo {username}!</span></h1>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 60px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="paragraph_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:5px;padding-left:60px;padding-right:60px;padding-top:5px;">
	<div style="color:#878787;direction:ltr;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size:24px;font-weight:400;letter-spacing:0px;line-height:200%;text-align:center;mso-line-height-alt:48px;">
	<p style="margin: 0;">Please click the button below to verify email address</p>
	</div>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 50px; padding-right: 50px; vertical-align: top; padding-top: 0px; padding-bottom: 40px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="10" cellspacing="0" class="button_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad">
	<div align="center" class="alignment">
	<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="Http://fashion-campus-gt20.my.id:5000/verify?uuid={uuid}" style="height:56px;width:247px;v-text-anchor:middle;" arcsize="8%" stroke="false" fillcolor="#3AAEE0"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Arial, sans-serif; font-size:23px"><![endif]--><a href="Http://fashion-campus-gt20.my.id:5000/verify?uuid={uuid}" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#3AAEE0;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:Poppins, Arial, Helvetica, sans-serif;font-size:23px;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:20px;padding-right:20px;font-size:23px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 46px;">Verify email address</span></span></a>
	<!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
	</div>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-left: 50px; padding-right: 50px; vertical-align: top; padding-top: 40px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="text_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:15px;padding-left:30px;padding-right:30px;padding-top:10px;">
	<div style="font-family: sans-serif">
	<div class="" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #888888; line-height: 1.2; font-family: Poppins, Arial, Helvetica, sans-serif;">
	<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:20px;">if you did not create an account, no furter action is required.</span></p>
	</div>
	</div>
	</td>
	</tr>
	</table>
	<table border="0" cellpadding="0" cellspacing="0" class="text_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:15px;padding-left:5px;padding-right:30px;padding-top:10px;">
	<div style="font-family: sans-serif">
	<div class="" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #888888; line-height: 1.2; font-family: Poppins, Arial, Helvetica, sans-serif;">
	<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="font-size:20px;">Regard,</span></p>
	</div>
	</div>
	</td>
	</tr>
	</table>
	<table border="0" cellpadding="0" cellspacing="0" class="heading_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:15px;padding-top:15px;text-align:center;width:100%;">
	<h3 style="margin: 0; color: #020b22; direction: ltr; font-family: Poppins, Arial, Helvetica, sans-serif; font-size: 24px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><strong><span class="tinyMce-placeholder"><span id="05276ec3-3f46-45fb-8f44-d2df8fd334b8">@startupcampuss</span></span></strong></h3>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-6" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f2f5ff; border-radius: 0 0 30px 30px; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 4ArnkyH51JRD2r6QNhraoYfZJ5vrwQh3dczAM6WnRm5P64CgwwDzXoffBJT7nNm1tVfDLn6UtNC7vbs39vQD6x7EU1CLaSY: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="heading_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad" style="padding-bottom:20px;padding-top:20px;text-align:center;width:100%;">
	<h2 style="margin: 0; color: #1a30eb; direction: ltr; font-family: Poppins, Arial, Helvetica, sans-serif; font-size: 20px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><span class="tinyMce-placeholder">Fashion Campuss</span></h2>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-7" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1a30eb; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 4ArnkyH51JRD2r6QNhraoYfZJ5vrwQh3dczAM6WnRm5P64CgwwDzXoffBJT7nNm1tVfDLn6UtNC7vbs39vQD6x7EU1CLaSY: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="20" cellspacing="0" class="text_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
	<tr>
	<td class="pad">
	<div style="font-family: sans-serif">
	<div class="" style="font-size: 12px; font-family: Poppins, Arial, Helvetica, sans-serif; mso-line-height-alt: 18px; color: #fafafa; line-height: 1.5;">
	<p style="margin: 0; font-size: 10px; text-align: center; mso-line-height-alt: 15px;"><span style="font-size:10px;"><span style="">© 2022 Fashion Campuss. </span></span><span style="font-size:10px;"><span style=""> All Rights Reserved.</span></span></p>
	</div>
	</div>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-8" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tbody>
	<tr>
	<td>
	<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680">
	<tbody>
	<tr>
	<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 4ArnkyH51JRD2r6QNhraoYfZJ5vrwQh3dczAM6WnRm5P64CgwwDzXoffBJT7nNm1tVfDLn6UtNC7vbs39vQD6x7EU1CLaSY0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
	<table border="0" cellpadding="0" cellspacing="0" class="icons_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="pad" style="vertical-align: middle; color: #9d9d9d; font-family: inherit; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;">
	<table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
	<tr>
	<td class="alignment" style="vertical-align: middle; text-align: center;">
	<!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
	<!--[if !vml]><!-->
	<table cellpadding="0" cellspacing="0" class="icons-inner" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;">
	<!--<![endif]-->
	<tr>
	</tr>
	</table>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table><!-- End -->
	</body>
	</html>
	"""

	result = f'{first}{mid}{end}'
	return result


# template redirect verif email
def verifEmailPage(username):
	
	first = f"""<!DOCTYPE html>

	<html>
	<head>
	<title></title>
	<meta charset="utf-8"/>
	<meta content="width=device-width" name="viewport"/>
	<link href="https://fonts.googleapis.com/css?family=Work+Sans" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@700&display=swap" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Alegreya" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Lora" rel="stylesheet" type="text/css"/>
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css"/>
	<style>
	"""
	mid = """
			.bee-row,
			.bee-row-content {
				position: relative
			}

			.bee-row-1,
			.bee-row-2,
			.bee-row-3,
			.bee-row-4,
			.bee-row-5 {
				background-repeat: no-repeat
			}

			body {
				background-color: #dce1f6;
				color: #000;
				font-family: Roboto, Tahoma, Verdana, Segoe, sans-serif
			}

			a {
				color: #0068a5
			}

			* {
				box-sizing: border-box
			}

			body,
			h1,
			p {
				margin: 0
			}

			.bee-row-content {
				max-width: 1230px;
				margin: 0 auto;
				display: flex
			}

			.bee-row-content .bee-col-w2 {
				flex-basis: 17%
			}

			.bee-row-content .bee-col-w8 {
				flex-basis: 67%
			}

			.bee-row-content .bee-col-w12 {
				flex-basis: 100%
			}

			.bee-button .content {
				text-align: center
			}

			.bee-button a,
			.bee-icon .bee-icon-label-right a,
			.bee-menu ul li a {
				text-decoration: none
			}

			.bee-divider {
				overflow: auto
			}

			.bee-divider .center {
				margin: 0 auto
			}

			.bee-menu ul {
				margin: 0;
				padding: 0
			}

			.bee-icon {
				display: inline-block;
				vertical-align: middle
			}

			.bee-icon .bee-content {
				display: flex;
				align-items: center
			}

			.bee-menu ul {
				list-style-type: none
			}

			.bee-menu ul.bee-horizontal li {
				display: inline-block
			}

			.bee-social .icon img {
				max-height: 32px
			}

			.bee-paragraph {
				overflow-wrap: anywhere
			}

			.bee-row-1 {
				background-color: #f6f7fc;
				background-position: top center
			}

			.bee-row-1 .bee-row-content,
			.bee-row-2 .bee-row-content,
			.bee-row-3 .bee-row-content,
			.bee-row-4 .bee-row-content,
			.bee-row-5 .bee-row-content {
				background-repeat: no-repeat;
				color: #000
			}

			.bee-row-1 .bee-col-1 {
				padding: 20px 10px 25px
			}

			.bee-row-2 .bee-col-1,
			.bee-row-3 .bee-col-1,
			.bee-row-3 .bee-col-2,
			.bee-row-3 .bee-col-3,
			.bee-row-4 .bee-col-1,
			.bee-row-5 .bee-col-1 {
				padding-bottom: 5px;
				padding-top: 5px
			}

			.bee-row-1 .bee-col-1 .bee-block-1,
			.bee-row-2 .bee-col-1 .bee-block-1,
			.bee-row-3 .bee-col-2 .bee-block-1 li,
			.bee-row-4 .bee-col-1 .bee-block-1 {
				padding: 10px
			}

			.bee-row-1 .bee-col-1 .bee-block-2 {
				padding: 10px;
				text-align: center;
				width: 100%
			}

			.bee-row-1 .bee-col-1 .bee-block-3 {
				padding: 15px
			}

			.bee-row-1 .bee-col-1 .bee-block-4,
			.bee-row-3 .bee-col-3 .bee-block-1 {
				padding: 10px;
				text-align: center
			}

			.bee-row-2,
			.bee-row-3,
			.bee-row-4 {
				background-color: #232846
			}

			.bee-row-3 .bee-col-2 {
				padding-right: 20px
			}

			.bee-row-3 .bee-col-2 .bee-block-1 {
				color: #fff;
				font-family: inherit;
				font-size: 14px;
				padding-bottom: 10px;
				padding-left: 15px;
				padding-top: 10px;
				text-align: center
			}

			.bee-row-5 .bee-col-1 .bee-block-1 {
				color: #9d9d9d;
				font-family: inherit;
				font-size: 15px;
				padding-bottom: 5px;
				padding-top: 5px;
				text-align: center
			}

			.bee-row-3 .bee-col-2 .bee-block-1 li a {
				color: #fff
			}

			@media (max-width:768px) {
				.bee-row-content:not(.no_stack) {
					display: block
				}
			}

			.bee-row-1 .bee-col-1 .bee-block-3 {
				color: #083d77;
				direction: ltr;
				font-size: 24px;
				font-weight: 400;
				letter-spacing: 0;
				line-height: 120%;
				text-align: center
			}

			.bee-row-1 .bee-col-1 .bee-block-3 a {
				color: #8a3b8f
			}

			.bee-row-1 .bee-col-1 .bee-block-3 p:not(:last-child) {
				margin-bottom: 16px
			}

			.bee-row-5 .bee-col-1 .bee-block-1 .bee-icon-image {
				padding: 5px 6px 5px 5px
			}

			.bee-row-5 .bee-col-1 .bee-block-1 .bee-icon:not(.bee-icon-first) .bee-content {
				margin-left: 0
			}

			.bee-row-5 .bee-col-1 .bee-block-1 .bee-icon::not(.bee-icon-last) .bee-content {
				margin-right: 0
			}
		</style>
		"""

	end = f"""
	</head>
	<body>
	<div class="bee-page-container">
	<div class="bee-row bee-row-1">
	<div class="bee-row-content">
	<div class="bee-col bee-col-1 bee-col-w12">
	<div class="bee-block bee-block-1 bee-divider">
	<div class="spacer" style="height:40px;"></div>
	</div>
	<div class="bee-block bee-block-2 bee-heading">
	<h1 style="color:#083d77;direction:ltr;font-family:'Lora', Georgia, serif ;font-size:55px;font-weight:400;letter-spacing:normal;line-height:120%;text-align:center;margin-top:0;margin-bottom:0;"><span class="tinyMce-placeholder">Thank you,<br/><span style="color: #536bcf;">{username}</span></span> </h1>
	</div>
	<div class="bee-block bee-block-3 bee-paragraph">
	<p>Your Email Has Been Verification.</p>
	<p>Please Login !</p>
	</div>
	<div class="bee-block bee-block-4 bee-button"><a class="bee-button-content" href="http://fashion-campus-gt20.my.id/Login" style="font-family: 'Lora', Georgia, serif; font-size: 22px; background-color: #536bcf; border-bottom: 0px solid #8A3B8F; border-left: 0px solid #8A3B8F; border-radius: 2px; border-right: 0px solid #8A3B8F; border-top: 0px solid #8A3B8F; color: #ffffff; font-weight: 4ArnkyH51JRD2r6QNhraoYfZJ5vrwQh3dczAM6WnRm5P64CgwwDzXoffBJT7nNm1tVfDLn6UtNC7vbs39vQD6x7EU1CLaSY: 5px; width: auto; direction: ltr; display: inline-block;"><span dir="ltr" style="word-break: break-word; font-size: 22px; line-height: 200%;"><span dir="ltr" style="font-size: 22px;">Click this</span></span></a></div>
	</div>
	</div>
	</div>
	<div class="bee-row bee-row-2">
	<div class="bee-row-content">
	<div class="bee-col bee-col-1 bee-col-w12">
	<div class="bee-block bee-block-1 bee-divider">
	<div class="spacer" style="height:16px;"></div>
	</div>
	</div>
	</div>
	</div>
	<div class="bee-row bee-row-3">
	<div class="bee-row-content">
	<div class="bee-col bee-col-1 bee-col-w2"></div>
	<div class="bee-col bee-col-2 bee-col-w8">
	<div class="bee-block bee-block-1 bee-menu">
	<nav class="bee-menu">
	<ul class="bee-horizontal">
	<li><a href="https://startupcampus.id" target="_self" title="">About us</a></li>
	</ul>
	</nav>
	</div>
	</div>
	<div class="bee-col bee-col-3 bee-col-w2">
	<div class="bee-block bee-block-1 bee-social">
	<div class="content"><span class="icon" style="padding:0 2.5px 0 2.5px;"><a href="https://m.facebook.com/startupcampusidn/"><img alt="Facebook" src="images/facebook2x.png" title="facebook"/></a></span><span class="icon" style="padding:0 2.5px 0 2.5px;"><a href="https://www.linkedin.com/school/startupcampusid/"><img alt="Linkedin" src="images/linkedin2x.png" title="linkedin"/></a></span><span class="icon" style="padding:0 2.5px 0 2.5px;"><a href="https://www.instagram.com/startupcampus.id/"><img alt="Instagram" src="images/instagram2x.png" title="instagram"/></a></span></div>
	</div>
	</div>
	</div>
	</div>
	<div class="bee-row bee-row-4">
	<div class="bee-row-content">
	<div class="bee-col bee-col-1 bee-col-w12">
	<div class="bee-block bee-block-1 bee-divider">
	<div class="spacer" style="height:16px;"></div>
	</div>
	</div>
	</div>
	</div>
	<div class="bee-row bee-row-5">
	<div class="bee-row-content">
	<div class="bee-col bee-col-1 bee-col-w12">
	<div class="bee-block bee-block-1 bee-icons">
	<div class="bee-icon bee-icon-last">
	<div class="bee-content">
	</div>
	</div>
	</div>
	</div>
	</div>
	</div>
	</div>
	</body>
	</html>
	"""
	
	result = f'{first}{mid}{end}'
	return result


# template if error verification
def errorPage():
	first = """
	<style>
	html { box-sizing: border-box; }

	*,
	*::before,
	*::after { box-sizing: inherit; }

	body * {
	margin: 0;
	padding: 0;
	}

	body {
	font: normal 100%/1.15 "Merriweather", serif;
	background-color: #7ed0f2;
	color: #fff;
	}

	.wrapper {
	position: relative;
	max-width: 1298px;
	height: auto;
	margin: 2em auto 0 auto;
	}

	/* https://www.flaticon.com/authors/vectors-market */
	/* https://www.flaticon.com/authors/icomoon */
	.box {
	max-width: 70%;
	min-height: auto;
	margin: 0 auto;
	padding: 1em 1em;
	text-align: center;
	background: url("https://www.dropbox.com/s/xq0841cp3icnuqd/flame.png?raw=1") no-repeat top 10em center/128px 128px,
				transparent url("https://www.dropbox.com/s/w7qqrcvhlx3pwnf/desktop-pc.png?raw=1") no-repeat top 13em center/128px 128px;
	}

	h1, p:not(:last-of-type) { text-shadow: 0 0 6px #216f79; }

	h1 {
	margin: 0 0 1rem 0;
	font-size: 8em;
	}

	p {
	margin-bottom: 0.5em;
	font-size: 3em;
	}

	p:first-of-type { margin-top: 4em; }

	p > a {
	border-bottom: 1px dashed #216f79;
	font-style: italic;
	text-decoration: none;
	color: #216f79;
	}

	p > a:hover { text-shadow: 0 0 6px #216f79; }

	p img { vertical-align: bottom; }

	</style>
	<div class="wrapper">
		<div class="box">
		<h1>500</h1>
		<p>Sorry, Your account not verified.</p>
		<p>&#58;&#40;</p>
		<p><a href="/">Cek again your email!</a></p>
		</div>
		</div>
	"""
	return first








