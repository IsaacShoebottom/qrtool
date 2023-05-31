import click
import pathlib
import segno

from segno import helpers

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
# Version, Input, Output, QR Text, QR Error Correction Level, QR Border, QR Scale, WiFi Helper
@click.option('-v', '--version', is_flag=True, help="Show version")
# Output file, required
@click.option('-o', '--output', type=pathlib.Path, required=True, help="Output file")
# QR Text, required
@click.option('-t', '--text', type=str, required=False, help="QR Text")
# QR Error Correction Level, values: L, M, Q, H, -, Not required, default: L
@click.option('-e', '--error-correction', default="L", type=str, required=False, help="QR error correction level")
# Border size, default: 4, Not required
@click.option('-b', '--border', type=int, default=4, required=False, help="QR border")
# QR Scale, default: 8, Not required
@click.option('-s', '--scale', type=int, default=8, required=False, help="QR scale")
# Wi-Fi switch, Not required
@click.option('-w', '--wifi', is_flag=True, required=False, help="Wi-Fi Flag, if enabled, it will parse the encryption, ssid and password options and generate a Wi-Fi QR code. What you put is taken literally, so make sure you put the right information.")
# Encryption type, Not required
@click.option('--encryption', type=click.Choice(["WEP", "WPA", "None"], case_sensitive=False), required=False, help="Wi-Fi encryption type")
# SSID, Not required
@click.option('--ssid', type=str, required=False, help="Wi-Fi SSID")
# Password, Not required
@click.option('--password', type=str, required=False, help="Wi-Fi password")
def cli(version, output, text, error_correction, border, scale, wifi, encryption, ssid, password):
    """QRTool - A simple QR code generator"""
    if not text and not wifi:
        print("Please provide text or Wi-Fi information")
        return
    if version:
        print("QRTool v0.1.0")
    if wifi:
        text = helpers.make_wifi_data(ssid, password, encryption)

    qr = segno.make_qr(content=text, error=error_correction)
    qr.save(output, border=border, scale=scale)
    print("QR code saved to: " + str(output))


if __name__ == '__main__':
    cli()
