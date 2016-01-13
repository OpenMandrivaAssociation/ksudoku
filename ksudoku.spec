Summary:	Play, create and solve sudoku grids
Name:		ksudoku
Version:	15.12.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/ksudoku/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs-devel
BuildRequires:	cmake(KDEGames)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)

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

%files
%{_bindir}/ksudoku
%{_datadir}/applications/kde4/ksudoku.desktop
%{_datadir}/apps/ksudoku
%{_datadir}/config/ksudokurc
%{_iconsdir}/hicolor/*/apps/ksudoku.png
%{_datadir}/appdata/*.xml
%doc %{_docdir}/*/*/ksudoku

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

