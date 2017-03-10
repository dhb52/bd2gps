; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{B013A105-A8E0-4F94-B4EE-04141D9858F8}}
AppName=bd2gps
AppVersion=0.1.0
;AppVerName=BD09 WGS84 Convertor
AppPublisher=Barry, Co.
DefaultDirName={pf}\bd2gps
DefaultGroupName=bd2gps
AllowNoIcons=yes
OutputBaseFilename="bd2gps-py2-qt4-setup_v0.1.0"
Compression=lzma
SolidCompression=yes

[Languages]
Name: "ChineseSimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "dist\bd2gps\bd2gps.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\bd2gps\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\bd2gps"; Filename: "{app}\bd2gps.exe"
Name: "{group}\{cm:UninstallProgram,bd2gps}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\bd2gps"; Filename: "{app}\bd2gps.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\bd2gps.exe"; Description: "{cm:LaunchProgram,bd2gps}"; Flags: nowait postinstall skipifsilent
