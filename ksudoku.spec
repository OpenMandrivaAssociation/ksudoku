%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Play, create and solve sudoku grids
Name:		ksudoku
Version:	 18.08.2
Release:	2
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/ksudoku/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(OpenGL)

%description
The word Sudoku means "single number in an alloted place" in Japanese. These
are the basic rules. Every sudoku Sudoku is a square of 81 cells divided into
9 columns and 9 rows and in 9 subsquares (3x3) of 9 cells each. Solving takes
usually from 10 to 30 minutes, depending on puzzle level, your skill and
experience.

Some cells are filled with a number at the beginnning: the remaining are to
be filled by the player using numbers from 1 to 9, without repeating a number
twice on each column, row or subsuquare (each of them must contain only
one 1, one 2, one 3, and so on). The game requires logic and patience.
The numerals in Sudoku puzzles are used for convenience (for example in 16x16
board we use letters): arithmetic relationships between numbers are irrelevant.

This program supports also 16x16 games with numbers from 1 to 16 and 256
cells with 16 cols, rows and subsquares! (if normal sudoku are not enough for
you).

More information at http://en.wikipedia.org/wiki/Sudoku

%files -f %{name}.lang
%{_bindir}/ksudoku
%{_datadir}/applications/*.desktop
%{_datadir}/ksudoku
%{_sysconfdir}/xdg/ksudokurc
%{_iconsdir}/hicolor/*/apps/ksudoku.png
%{_datadir}/metainfo/*.xml
%{_datadir}/kxmlgui5/ksudoku

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
