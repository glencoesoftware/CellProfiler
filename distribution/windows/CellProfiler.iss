; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "CellProfiler"
#define MyAppPublisher "Broad Institute"
#define MyAppURL "http://cellprofiler.org/"
#define MyAppExeName "CellProfiler.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{4948C255-0E77-4A37-B88D-F0A5BAD13CF4}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf64}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=..\..\LICENSE
OutputBaseFilename=CellProfiler-Windows-{#MyAppVersion}
SetupIconFile=..\..\cellprofiler\data\icons\CellProfiler.ico
UninstallDisplayIcon={app}\cellprofiler\data\icons\CellProfiler.ico
Compression=lzma
SolidCompression=yes
DisableDirPage=no
ChangesEnvironment=yes
ChangesAssociations=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\..\dist\CellProfiler\CellProfiler.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\dist\CellProfiler\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#JavaDir}\x64\*"; DestDir: "{app}\java"; Flags: recursesubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Registry]
Root: HKA; Subkey: "Software\Classes\.cpproj\OpenWithProgids"; ValueType: string; ValueName: "CellProfiler.cpproj"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\.cppipe\OpenWithProgids"; ValueType: string; ValueName: "CellProfiler.cppipe"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\CellProfiler.cpproj"; ValueType: string; ValueName: ""; ValueData: "CellProfiler Project"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\CellProfiler.cppipe"; ValueType: string; ValueName: ""; ValueData: "CellProfiler Pipeline"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\CellProfiler.cpproj\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\CellProfiler.exe,0"
Root: HKA; Subkey: "Software\Classes\CellProfiler.cppipe\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\CellProfiler.exe,0"
Root: HKA; Subkey: "Software\Classes\CellProfiler.cpproj\shell\open\command"; ValueType: string; ValueName: ""; ValueData: "cmd /c ""{drive:{app}} & ""{app}\CellProfiler.exe"" ""%1"""""
Root: HKA; Subkey: "Software\Classes\CellProfiler.cppipe\shell\open\command"; ValueType: string; ValueName: ""; ValueData: "cmd /c ""{drive:{app}} & ""{app}\CellProfiler.exe"" ""%1"""""
Root: HKA; Subkey: "Software\Classes\Applications\CellProfiler.exe\SupportedTypes"; ValueType: string; ValueName: ".cpproj"; ValueData: ""
Root: HKA; Subkey: "Software\Classes\Applications\CellProfiler.exe\SupportedTypes"; ValueType: string; ValueName: ".cppipe"; ValueData: ""