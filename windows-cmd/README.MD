# Windows command line
## calculator.bat (batch file, conditionals, command line arguments)

calculator.bat demostrates how to use command line arguments inside batch file and usage of conditionals.
calculator.bat faylı batch fayllarında command line arqumentlərlə, şərtlərlə işləməyi nümayiş etdirir.

`calculator.bat add 1 2` - should output 3, terminal ekranına 3 çap etməlidir

`calculator.bat sub 1 2` - should output -1, terminal ekranına -1 çap etməlidir

## System

`driverquery -v` - list the installed drivers, quraşdırılmış drayverlərə baxmaq

`systeminfo` - hardware information, sistem məlumatlarını göstərmək

`sfc /scannow` - scan and repair system, sistem xətaları tapmaq və aradan qaldırmaq

`CHKDSK /f C:` - scan and repair drive, disklə əlaqədar xətaları tapmaq və aradan qaldırmaq

`tasklist` - view task list, proseslərin siyahısını çap etmək

`cls` - clear screen, terminal ekranını təmizləmək

## Network

`ping` - send packets to server for testing reachibility, serverlə əlaqəni yoxlamaq üçün paketlər göndərmək

`netstat` - display network connections, şəbəkə bağlantılarını göstərmək

`nslookup` - dns lookups, resursun dns məlumatlarını əldə etmək

`telnet` - establish connection, digər serverlə əlaqə qurmaq

`ipconfig` - display network configuration, şəbəkə məlumatların (ip konfiqurasiya və s.)

## File system, navigation

`cd` - cd working directory, cari qovluğu dəyişmək üçün istifadə olunur

`cd ..` - go one level up, qovluqlar iyerarxiyasında bir səviyyə yuxarı qalxmaq üçün

`mkdir` - create new directory, yeni qovluq düzəltmək üçün

`dir` - list contents of working directory, cari qovluğun tərkibini çap edir

`move` - move folder/file, qovluğu/faylı digər qovluğa göndərmək üçün

`copy` - copy folder/file

`rename` - rename files, ad dəyişmək üçün

`rmdir` - remove directory (add /s option to remove non-empty folder), qovluğu silmək üçün (boş olmayan qovluğu silmək üçün /s əlavə edin), 

`D:` - change current drive (by typing its letter), cari diski (drive) dəyişmək üçün (simvolunu yazmaqla)

## Loops

`for /l %x in (1, 1, 100) do echo %x` - start with 1, increment by 1, stop at 100, print each time, 1-lə başla, vahid artımla 100-ə kimi çap et

`for %f in (*) do echo %f` - list files in current directory (/R to include subdirs, /D to list directories), cari qovluqda faylları çap et

`type path_to_file` - output content of file, faylın mətnini çap et

`find, findstr` - search for a string in given file(s), verilmiş fayl(lar)-ın mətnində axtarış etmək üçün

`type C:\Users\USER\Desktop\sample.txt | find "" /v /c` - count number of lines in a file, faylda sətir sayını çap etmək üçün

## autostart

To add program into startup: Win+R, then type `shell:startup`. Copy __windows-cmd/show_msg.bat__ file into the startup folder. Now the message will popup on every sign-in.