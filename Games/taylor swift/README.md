taylor swift
=============================================

This folder contains a recreation of popular games written in Swift.

-------------------------------------------
conwayv4 (Cell: Game of Life / Conway's Game of Life)
-------------------------------------------
Build & Run:

Create a new XCode project and name the project "cell" (or anything you'd like)

Delete your "ContentView.swift" and replace that file with conwayv4's "ContentView.swift".

Click on your "Assets" and drag and drop "AppIcon-1.appiconset" into your "Assets".

Click on "cell" (not the folder but the .xcodeproj) in Xcode and change the display name to
"Cell: Game of Life" and App Icon Source to "Appicon-1"

Drag and drop conwayv4's "sounds" folder into your "cell" folder.

Connect your iPhone to your computer. Select your iPhone at the top of Xcode and press the play button
(Build on your device).

NOTE:
- Do NOT use iPad or other IOS devices besides an iPhone as the app will have an awkward appearance and potentially fail to build.
- When building, ensure your device is on and unlocked. The App will open and run at the end of the build.


Short: Play Conway's Game of Life on a 20x13 (or 15x9 if on a "mini" iPhone) grid. This is slightly
different from the typical Conway's Game of Life in which the grid is infinite. This allows the players
to develop new patterns by using the edges of the grid.

Long: The Game of Life is a cellular automaton created by John Conway in the 70s.
It is a zero-player game where each cell in a grid is either alive (filled) or dead (empty).
You can determine the initial state of the grid by clicking on which cells are alive or dead.
Then, click on the play button to see which cells live on to the next generation.

Conditions for a cell to be alive in the next generation:

1) If an alive cell has 2 or 3 neighbors, it will live to the next generation.

2) If an alive cell has less than 2 neighbors, it will die, as if by underpopulation.
 
3) If an alive cell has more than 3 neighbors, it will die, as if by overpopulation.

4) If a dead cell has 3 neighbors, it will become alive, as if by reproduction.
