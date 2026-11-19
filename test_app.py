from app import hello_world

def test_output():
    hasil = hello_world()
    assert "Hello, World!" in hasil, f"Validasi gagal, output tidak sesuai: {hasil}"
    print("Pengujian berhasil: Aplikasi memenuhi standar rilis.")

if __name__ == "__main__":
    test_output()
