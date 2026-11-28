; Inno Setup script for the APL installer (Windows).
; Built by the build workflow:  iscc /DAppVersion=... /DSourceDir=... /DOutDir=... packaging\apl.iss
#define AppName "APL"
#ifndef AppVersion
  #define AppVersion "1.0.0-dev"
#endif

[Setup]
AppId={{6C3D1E0B-4A77-4F0E-9B52-0A1B2C3D4E5F}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher=Ammar Elkhateeb
AppPublisherURL=https://ammarbasha2011.github.io/APL/
AppSupportURL=https://github.com/AmmarBasha2011/APL
DefaultDirName={autopf}\APL
DefaultGroupName=APL
UninstallDisplayIcon={app}\icons\apl.ico
SetupIconFile={#SourceDir}\icons\apl.ico
OutputDir={#OutDir}
OutputBaseFilename=APL-Setup-{#AppVersion}
Compression=lzma2
SolidCompression=yes
; Per-user install: no administrator prompt, and PATH is the user's own.
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
ChangesEnvironment=yes
ChangesAssociations=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64compatible

[Tasks]
Name: "desktopicon"; Description: "أيقونة APL REPL على سطح المكتب"; Flags: unchecked
Name: "associate"; Description: "فتح ملفات .apl بـ APL"; Flags: checkedonce

[Files]
Source: "{#SourceDir}\apl.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SourceDir}\apl.exe"; DestDir: "{app}"; DestName: "عمار.exe"; Flags: ignoreversion
Source: "{#SourceDir}\APL-Docs\*"; DestDir: "{app}\APL-Docs"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#SourceDir}\icons\*.ico"; DestDir: "{app}\icons"; Flags: ignoreversion

[Icons]
Name: "{group}\APL Terminal"; Filename: "{app}\apl.exe"; Parameters: "terminal"; IconFilename: "{app}\icons\terminal.ico"; Comment: "Terminal with proper Arabic"
Name: "{group}\APL REPL"; Filename: "{app}\apl.exe"; Parameters: "repl"; IconFilename: "{app}\icons\repl.ico"; Comment: "Try APL commands directly"
Name: "{group}\APL Libraries"; Filename: "{app}\apl.exe"; Parameters: "libraries"; IconFilename: "{app}\icons\libraries.ico"; Comment: "The libraries we maintain"
Name: "{group}\APL Docs"; Filename: "{app}\apl.exe"; Parameters: "docs"; IconFilename: "{app}\icons\docs.ico"; Comment: "Offline docs"
Name: "{group}\APL Examples"; Filename: "{app}\apl.exe"; Parameters: "examples"; IconFilename: "{app}\icons\examples.ico"; Comment: "Browse, copy and run examples"
Name: "{group}\APL Benchmark"; Filename: "{app}\apl.exe"; Parameters: "benchmark"; IconFilename: "{app}\icons\benchmark.ico"; Comment: "Speed benchmark"
Name: "{group}\Uninstall APL"; Filename: "{uninstallexe}"
Name: "{autodesktop}\APL REPL"; Filename: "{app}\apl.exe"; Parameters: "repl"; IconFilename: "{app}\icons\repl.ico"; Tasks: desktopicon

[Registry]
; PATH: add the install folder once.
Root: HKCU; Subkey: "Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Check: NeedsAddPath(ExpandConstant('{app}'))
; .apl files
Root: HKA; Subkey: "Software\Classes\.apl"; ValueType: string; ValueData: "APL.Program"; Flags: uninsdeletevalue; Tasks: associate
Root: HKA; Subkey: "Software\Classes\APL.Program"; ValueType: string; ValueData: "APL program"; Flags: uninsdeletekey; Tasks: associate
Root: HKA; Subkey: "Software\Classes\APL.Program\DefaultIcon"; ValueType: string; ValueData: "{app}\icons\apl.ico"; Tasks: associate
Root: HKA; Subkey: "Software\Classes\APL.Program\shell\open\command"; ValueType: string; ValueData: """{app}\apl.exe"" run ""%1"""; Tasks: associate

[Run]
Filename: "{app}\apl.exe"; Parameters: "repl"; Description: "تشغيل APL REPL"; Flags: postinstall nowait skipifsilent unchecked

[Code]
function NeedsAddPath(Param: string): Boolean;
var
  Existing: string;
begin
  if not RegQueryStringValue(HKCU, 'Environment', 'Path', Existing) then
  begin
    Result := True;
    exit;
  end;
  Result := Pos(';' + Lowercase(Param) + ';', ';' + Lowercase(Existing) + ';') = 0;
end;

procedure RemoveFromPath(Param: string);
var
  Existing, Cleaned: string;
  P: Integer;
begin
  if not RegQueryStringValue(HKCU, 'Environment', 'Path', Existing) then exit;
  Cleaned := ';' + Existing + ';';
  P := Pos(';' + Lowercase(Param) + ';', Lowercase(Cleaned));
  if P = 0 then exit;
  Delete(Cleaned, P, Length(Param) + 1);
  if (Length(Cleaned) > 0) and (Cleaned[1] = ';') then Delete(Cleaned, 1, 1);
  if (Length(Cleaned) > 0) and (Cleaned[Length(Cleaned)] = ';') then Delete(Cleaned, Length(Cleaned), 1);
  RegWriteExpandStringValue(HKCU, 'Environment', 'Path', Cleaned);
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usPostUninstall then
    RemoveFromPath(ExpandConstant('{app}'));
end;
