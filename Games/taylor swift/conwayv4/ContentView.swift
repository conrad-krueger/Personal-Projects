//
//  ContentView.swift
//  conwayv4
//
//  Created by Conrad Krueger on 6/4/22.
//
//

import SwiftUI
import AVFoundation
import UIKit


/**
    Used primarly for shrinking the grid size if iphone screen is too small...
    https://stackoverflow.com/questions/26028918/how-to-determine-the-current-iphone-device-model
*/
public extension UIDevice {

    static let modelName: String = {
        var systemInfo = utsname()
        uname(&systemInfo)
        let machineMirror = Mirror(reflecting: systemInfo.machine)
        let identifier = machineMirror.children.reduce("") { identifier, element in
            guard let value = element.value as? Int8, value != 0 else { return identifier }
            return identifier + String(UnicodeScalar(UInt8(value)))
        }

        func mapToDevice(identifier: String) -> String {
            #if os(iOS)
            switch identifier {
            case "iPod5,1":                                       return "iPod touch (5th generation)"
            case "iPod7,1":                                       return "iPod touch (6th generation)"
            case "iPod9,1":                                       return "iPod touch (7th generation)"
            case "iPhone3,1", "iPhone3,2", "iPhone3,3":           return "iPhone 4"
            case "iPhone4,1":                                     return "iPhone 4s"
            case "iPhone5,1", "iPhone5,2":                        return "iPhone 5"
            case "iPhone5,3", "iPhone5,4":                        return "iPhone 5c"
            case "iPhone6,1", "iPhone6,2":                        return "iPhone 5s"
            case "iPhone7,2":                                     return "iPhone 6"
            case "iPhone7,1":                                     return "iPhone 6 Plus"
            case "iPhone8,1":                                     return "iPhone 6s"
            case "iPhone8,2":                                     return "iPhone 6s Plus"
            case "iPhone9,1", "iPhone9,3":                        return "iPhone 7"
            case "iPhone9,2", "iPhone9,4":                        return "iPhone 7 Plus"
            case "iPhone10,1", "iPhone10,4":                      return "iPhone 8"
            case "iPhone10,2", "iPhone10,5":                      return "iPhone 8 Plus"
            case "iPhone10,3", "iPhone10,6":                      return "iPhone X"
            case "iPhone11,2":                                    return "iPhone XS"
            case "iPhone11,4", "iPhone11,6":                      return "iPhone XS Max"
            case "iPhone11,8":                                    return "iPhone XR"
            case "iPhone12,1":                                    return "iPhone 11"
            case "iPhone12,3":                                    return "iPhone 11 Pro"
            case "iPhone12,5":                                    return "iPhone 11 Pro Max"
            case "iPhone13,1":                                    return "iPhone 12 mini"
            case "iPhone13,2":                                    return "iPhone 12"
            case "iPhone13,3":                                    return "iPhone 12 Pro"
            case "iPhone13,4":                                    return "iPhone 12 Pro Max"
            case "iPhone14,4":                                    return "iPhone 13 mini"
            case "iPhone14,5":                                    return "iPhone 13"
            case "iPhone14,2":                                    return "iPhone 13 Pro"
            case "iPhone14,3":                                    return "iPhone 13 Pro Max"
            case "iPhone8,4":                                     return "iPhone SE"
            case "iPhone12,8":                                    return "iPhone SE (2nd generation)"
            case "iPhone14,6":                                    return "iPhone SE (3rd generation)"
            case "iPad2,1", "iPad2,2", "iPad2,3", "iPad2,4":      return "iPad 2"
            case "iPad3,1", "iPad3,2", "iPad3,3":                 return "iPad (3rd generation)"
            case "iPad3,4", "iPad3,5", "iPad3,6":                 return "iPad (4th generation)"
            case "iPad6,11", "iPad6,12":                          return "iPad (5th generation)"
            case "iPad7,5", "iPad7,6":                            return "iPad (6th generation)"
            case "iPad7,11", "iPad7,12":                          return "iPad (7th generation)"
            case "iPad11,6", "iPad11,7":                          return "iPad (8th generation)"
            case "iPad12,1", "iPad12,2":                          return "iPad (9th generation)"
            case "iPad4,1", "iPad4,2", "iPad4,3":                 return "iPad Air"
            case "iPad5,3", "iPad5,4":                            return "iPad Air 2"
            case "iPad11,3", "iPad11,4":                          return "iPad Air (3rd generation)"
            case "iPad13,1", "iPad13,2":                          return "iPad Air (4th generation)"
            case "iPad13,16", "iPad13,17":                        return "iPad Air (5th generation)"
            case "iPad2,5", "iPad2,6", "iPad2,7":                 return "iPad mini"
            case "iPad4,4", "iPad4,5", "iPad4,6":                 return "iPad mini 2"
            case "iPad4,7", "iPad4,8", "iPad4,9":                 return "iPad mini 3"
            case "iPad5,1", "iPad5,2":                            return "iPad mini 4"
            case "iPad11,1", "iPad11,2":                          return "iPad mini (5th generation)"
            case "iPad14,1", "iPad14,2":                          return "iPad mini (6th generation)"
            case "iPad6,3", "iPad6,4":                            return "iPad Pro (9.7-inch)"
            case "iPad7,3", "iPad7,4":                            return "iPad Pro (10.5-inch)"
            case "iPad8,1", "iPad8,2", "iPad8,3", "iPad8,4":      return "iPad Pro (11-inch) (1st generation)"
            case "iPad8,9", "iPad8,10":                           return "iPad Pro (11-inch) (2nd generation)"
            case "iPad13,4", "iPad13,5", "iPad13,6", "iPad13,7":  return "iPad Pro (11-inch) (3rd generation)"
            case "iPad6,7", "iPad6,8":                            return "iPad Pro (12.9-inch) (1st generation)"
            case "iPad7,1", "iPad7,2":                            return "iPad Pro (12.9-inch) (2nd generation)"
            case "iPad8,5", "iPad8,6", "iPad8,7", "iPad8,8":      return "iPad Pro (12.9-inch) (3rd generation)"
            case "iPad8,11", "iPad8,12":                          return "iPad Pro (12.9-inch) (4th generation)"
            case "iPad13,8", "iPad13,9", "iPad13,10", "iPad13,11":return "iPad Pro (12.9-inch) (5th generation)"
            case "AppleTV5,3":                                    return "Apple TV"
            case "AppleTV6,2":                                    return "Apple TV 4K"
            case "AudioAccessory1,1":                             return "HomePod"
            case "AudioAccessory5,1":                             return "HomePod mini"
            case "i386", "x86_64", "arm64":                       return "Simulator \(mapToDevice(identifier: ProcessInfo().environment["SIMULATOR_MODEL_IDENTIFIER"] ?? "iOS"))"
            default:                                              return identifier
            }
            #elseif os(tvOS)
            switch identifier {
            case "AppleTV5,3": return "Apple TV 4"
            case "AppleTV6,2": return "Apple TV 4K"
            case "i386", "x86_64": return "Simulator \(mapToDevice(identifier: ProcessInfo().environment["SIMULATOR_MODEL_IDENTIFIER"] ?? "tvOS"))"
            default: return identifier
            }
            #endif
        }

        return mapToDevice(identifier: identifier)
    }()

}


/**
 In case of scaling issues on any given iphone, the user is able to shrink and expand the view of the entire grid
 - notes: made slight modifications than what is show in given link below
 https://stackoverflow.com/questions/58341820/isnt-there-an-easy-way-to-pinch-to-zoom-in-an-image-in-swiftui
 */

struct ZoomableScrollView<Content: View>: UIViewRepresentable {
  private var content: Content


  init(@ViewBuilder content: () -> Content) {
    self.content = content()
  }

  func makeUIView(context: Context) -> UIScrollView {
    // set up the UIScrollView
    let scrollView = UIScrollView()
    scrollView.delegate = context.coordinator  // for viewForZooming(in:)
    scrollView.maximumZoomScale = 20
    scrollView.minimumZoomScale = 0.8
    scrollView.bouncesZoom = true

    // create a UIHostingController to hold our SwiftUI content
    let hostedView = context.coordinator.hostingController.view!
    hostedView.translatesAutoresizingMaskIntoConstraints = true
    hostedView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
    hostedView.frame = scrollView.bounds
    scrollView.addSubview(hostedView)

    return scrollView
  }

  func makeCoordinator() -> Coordinator {
    return Coordinator(hostingController: UIHostingController(rootView: self.content))
  }

  func updateUIView(_ uiView: UIScrollView, context: Context) {
    // update the hosting controller's SwiftUI content
    context.coordinator.hostingController.rootView = self.content
    assert(context.coordinator.hostingController.view.superview == uiView)
  }

  // MARK: - Coordinator

  class Coordinator: NSObject, UIScrollViewDelegate {
    var hostingController: UIHostingController<Content>

    init(hostingController: UIHostingController<Content>) {
      self.hostingController = hostingController
    }

    func viewForZooming(in scrollView: UIScrollView) -> UIView? {
      return hostingController.view
    }
  }
}

struct ScrollView<Content: View>: UIViewRepresentable {
  private var content: Content

  init(@ViewBuilder content: () -> Content) {
    self.content = content()
  }

  func makeUIView(context: Context) -> UIScrollView {
    // set up the UIScrollView
    let scrollView = UIScrollView()
    scrollView.delegate = context.coordinator  // for viewForZooming(in:)
    scrollView.maximumZoomScale = 1
      scrollView.minimumZoomScale = 1
    scrollView.bouncesZoom = true

    // create a UIHostingController to hold our SwiftUI content
    let hostedView = context.coordinator.hostingController.view!
    hostedView.translatesAutoresizingMaskIntoConstraints = true
    hostedView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
    hostedView.frame = scrollView.bounds
    scrollView.addSubview(hostedView)

    return scrollView
  }

  func makeCoordinator() -> Coordinator {
    return Coordinator(hostingController: UIHostingController(rootView: self.content))
  }

  func updateUIView(_ uiView: UIScrollView, context: Context) {
    // update the hosting controller's SwiftUI content
    context.coordinator.hostingController.rootView = self.content
    assert(context.coordinator.hostingController.view.superview == uiView)
  }

  // MARK: - Coordinator

  class Coordinator: NSObject, UIScrollViewDelegate {
    var hostingController: UIHostingController<Content>

    init(hostingController: UIHostingController<Content>) {
      self.hostingController = hostingController
    }

    func viewForZooming(in scrollView: UIScrollView) -> UIView? {
      return hostingController.view
    }
  }
}


/*All my code starting from here*/


var player: AVAudioPlayer! //for playing audio

let small = (UIDevice.modelName == "iPhone 13 mini" ||  UIDevice.modelName == "iPhone 12 mini") //bool for determining grid size

//grid size dimensions
var dimX = small ? 9 : 13
var dimY = small ? 15 : 20

//options to place blocks on title screen
var opX:[Int] = [30,60,90,120,150,180,210,240,270,300,330,360,390,420,450]
var opY:[Int] = [30,60,90,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570,600,630,660,690,720,750,780]



struct ContentView: View {
    
    @State var opac = 0.75 //opacity of non filled blocks
    
    @State var play = false //bool if play button was pressed
    @State var titleScreen = true //bool if title screen is shown
    @State var M: Int = dimX
    @State var N: Int = dimY

    @State var time = 0.35 //time between current grid and next grid

    @State var grid:[[Bool]] = [[Bool]](repeating:[Bool](repeating:false,count:dimY),count:dimX) //actual grid (false = dead cell, true = alive cell)

    @Environment(\.colorScheme) var colorScheme
    
    /**
     Generates random dispersion of alive particles on a grid
     - parameter prob: probability that any given cell is alive
     - update: grid
     */
    func randomGen(_ prob:Int){
        clear()
        for i in 0...M-1{
            for j in 0...N-1{
                if (Int.random(in: 1...100) <= prob){
                    grid[i][j] = true
                }
            }
        }
    }
    
    
    /**
     Returns the number of neighbors of any given cell
     - parameter x: x-coordinate of cell
     - parameter y: y-coordinate of cell
     - returns:  int number of neighbors
     */
    func getNeighbors(_ x:Int, _ y:Int) -> Int{
      var count = 0
      if(x-1 >= 0){
        //top
        if grid[x-1][y]{
            count += 1
        }
        if(y-1 >= 0 && grid[x-1][y-1]){ //top left
            count += 1
        }

        if(y+1 < N && grid[x-1][y+1]){ //top right
          count += 1
        }
      }

      if(y-1 >= 0 && grid[x][y-1]){ //left
          count += 1
      }

      if(y+1 < N && grid[x][y+1]){ //right
          count += 1
      }
      
      if(x+1 < M){
        //bottom
        if(grid[x+1][y]){
            count += 1
        }

        if(y-1 >= 0 && grid[x+1][y-1]){ //bottom left
          count += 1
        }

        if(y+1 < N && grid[x+1][y+1]){ //bottom right
          count += 1
        }
      }
      return count
    }
    
    /**
     Generates next grid based on current grids cell configuration. Uses Conway's rules to determine which cells will appear
        in the next grid (next generation)
     - returns:  list of a list of booleans that will replace the previous grid
     */
    func nextGrid() -> [[Bool]]{
        let row = [Bool](repeating:false,count:N)
        var gridNew = [[Bool]](repeating:row,count:N)
        
        for i in 0...M-1{
            for j in 0...N-1{
                let neighbors = getNeighbors(i,j)
                if ((neighbors == 2 && grid[i][j]) || neighbors == 3){
                    gridNew[i][j] = true
                }
            }
        }
        return gridNew
        
    }
    
    /**
     Kills all cells in grid (sets each enry in grid to false)
        - update: grid
     */
    func clear(){
        for i in 0...M-1{
            for j in 0...N-1{
                grid[i][j] = false
            }
        }
    }
    
    /**
     Sets a grid to contain a pre-determined pattern
       - parameter name: name of pattern
       - parameter x: x displacement of pattern
       - parameter y: y displacement of pattern
        - update: grid
     */
    func pattern(_ name:String, _ x:Int, _ y:Int){
        clear() //erase
        var displaceX = x
        var displaceY = y
        
        if small{
            displaceX-=2
            displaceY-=3
            
        }
        if (name == "gliders"){
            grid[2][0] = true
            grid[2][1] = true
            grid[2][2] = true
            grid[1][2] = true
            grid[0][1] = true
            
            grid[2][5] = true
            grid[2][6] = true
            grid[2][7] = true
            grid[1][7] = true
            grid[0][6] = true
        }
        else if (name == "pentadecathlon"){
            
            grid[displaceX+6][displaceY+9] = true
            grid[displaceX+6][displaceY+10] = true
            grid[displaceX+6][displaceY+11] = true
            grid[displaceX+6][displaceY+8] = true
            
            grid[displaceX+5][displaceY+12] = true
            grid[displaceX+7][displaceY+12] = true
            
            grid[displaceX+5][displaceY+7] = true
            grid[displaceX+7][displaceY+7] = true
            
            grid[displaceX+6][displaceY+13] = true
            grid[displaceX+6][displaceY+14] = true
            
            grid[displaceX+6][displaceY+6] = true
            grid[displaceX+6][displaceY+5] = true
            
        }
        else if (name == "multiplier"){
            grid[displaceX+6][displaceY+11] = true
            grid[displaceX+6][displaceY+9] = true
            grid[displaceX+7][displaceY+9] = true
            grid[displaceX+7][displaceY+11] = true
            grid[displaceX+6][displaceY+10] = true
            grid[displaceX+5][displaceY+10] = true
            grid[displaceX+8][displaceY+10] = true
        }
        else if (name == "beacon"){
            grid[displaceX+4][displaceY+9] = true
            grid[displaceX+5][displaceY+9] = true
            grid[displaceX+4][displaceY+8] = true
            grid[displaceX+5][displaceY+8] = true
            
            grid[displaceX+6][displaceY+11] = true
            grid[displaceX+7][displaceY+11] = true
            grid[displaceX+6][displaceY+10] = true
            grid[displaceX+7][displaceY+10] = true
        }
        else if (name == "multiplier + squares"){
            grid[displaceX+4][displaceY+17] = true
            grid[displaceX+4][displaceY+16] = true
            grid[displaceX+5][displaceY+17] = true
            grid[displaceX+5][displaceY+16] = true
            
            grid[displaceX+7][displaceY+17] = true
            grid[displaceX+7][displaceY+16] = true
            grid[displaceX+8][displaceY+17] = true
            grid[displaceX+8][displaceY+16] = true
            
            grid[displaceX+6][displaceY+12] = true
            grid[displaceX+7][displaceY+11] = true
            grid[displaceX+5][displaceY+11] = true
            grid[displaceX+6][displaceY+11] = true
            grid[displaceX+7][displaceY+10] = true
            grid[displaceX+5][displaceY+10] = true
            grid[displaceX+6][displaceY+9] = true
            
            
        }
        else{
            randomGen(25)
        }
        
        
    }
    
    /**
     Plays clicking sound which indicates a new generation has passed
     */
    
    func sound(){
        let url = Bundle.main.url(forResource: "click", withExtension: "mp3")
        guard url != nil else{
            return
        }
        
        do{
            player = try AVAudioPlayer(contentsOf: url!)
            player?.play()
        }catch{
            print("ERR")
        }
        
    }
    
    /**
     Plays sound which indicates certain buttons have been pressed
     */
    func soundButton(){
        let url = Bundle.main.url(forResource: "mixkit-modern-click-box-check-1120", withExtension: "wav")
        guard url != nil else{
            return
        }
        
        do{
            player = try AVAudioPlayer(contentsOf: url!)
            player?.play()
        }catch{
            print("ERR")
        }
        
    }
    
    
    

    var body: some View {
        
        ZStack{
            
            let timer = Timer.publish(every: time, on: .main, in: .common).autoconnect()
            let color = (colorScheme == .dark) ? Color.white : Color.black
            
            
            VStack{
                
                ZoomableScrollView{
                    
                    
                HStack(spacing: 0.05){
                    
                    Spacer()
                    
                    //Show the grid
                    
                    ForEach (0...dimX-1, id: \.self){ i in
                        VStack{
                            Spacer()
                            ForEach (0...dimY-1, id: \.self){ j in
                                let name = grid[i][j] ? "square.fill": "square" //filled square = true = alive
                                Button (action: { //each grid square is a button that can be pressed by the user
                                    if (grid[i][j] == true){
                                        grid[i][j] = false
                                    }else{
                                        grid[i][j] = true
                                    }
                                }, label: {
                                    Image(systemName: name).foregroundColor(grid[i][j] ? color.opacity(0.9): Color.gray.opacity(0.5)).scaleEffect(1.3).scaleEffect(small ? 1.15 : 1.3).padding(.horizontal,2.2).padding(.vertical,-1) //visual appearance mods
                                }).opacity(grid[i][j] || !play ? 1 : 0).buttonStyle(.plain)
                            }
                            Spacer()
                            Spacer()
                        }
                    }
                    Spacer()
                        
                }
                }
                Spacer()
                Text("").foregroundColor(Color.white).onReceive(timer, perform: {_ in //hidden text that continually updates the grid and plays sound()
                    if play{
                        grid = nextGrid()
                        sound()
                    }else{
                        play = false
                    }}).padding(-150)
                Spacer()
                HStack{
                    HStack{
                        Spacer()
                        
                        //Clear button (calls clear())
                        Button {
                            if !play{
                                clear()
                            }
                        } label: {
                            Image(systemName:"trash" ).scaleEffect(1.25).padding(.bottom).opacity(play ? 0 : 1)
                        }.buttonStyle(.plain).foregroundColor(Color.blue)
                        Spacer()
                        //Shuffle button (calls randomGen())
                        Button {
                            if !play{
                                randomGen(Int.random(in: 25...40))
                            }
                            
                        } label: {
                            Image(systemName: "shuffle").scaleEffect(1.25).padding(.bottom).opacity(play ? 0 : 1)
                        }.buttonStyle(.plain).foregroundColor(Color.blue)
                        Spacer()
                    }
                    Spacer()
                    
                    //Play Button (shows next generations until button is pressed again)
                    Button {
                        play = !play
                        soundButton()
                
                    } label: {
                        Image(systemName: play ? "pause" : "play.fill" ).scaleEffect(2).padding(.bottom).foregroundColor(color)
                    }.buttonStyle(.plain)
                    
                    Spacer()
                    HStack{
                        Spacer()
                        
                        //Menu to selected prewritten patterns (calls pattern())
                        Menu {
                            Button(action: {pattern("beacon",0,0)}, label: {Text("Beacon")})
                            Button(action: {pattern("gliders",0,0)}, label: {Text("Gliders")})
                            if !small{Button(action: {pattern("pentadecathlon",0,0)}, label: {Text("Pentadecathlon")})}
                            Button(action: {pattern("multiplier",0,0)}, label: {Text("Multiplier")})
                            Button(action: {pattern("multiplier + squares",0,0)}, label: {Text("Multiplier + Squares")})
                            
                        } label: {
                            Image(systemName:"folder" ).scaleEffect(1.25).padding(.bottom).opacity(play ? 0 : 1)
                        }
                        Spacer()
                    
                    }
                    
                    Spacer()
                }
                Spacer()
                
            }
            
            //Title Screen apperance
            if titleScreen{
                
                Color.black.ignoresSafeArea()
                
                ZStack{
                    ForEach(1...100, id: \.self){ i in
                        let randx = Int.random(in: 0...14)
                        let randy = Int.random(in: 0...24)
                        Image(systemName: "square").foregroundColor(Color.gray).scaleEffect(small ? 1 : 2).position(x: CGFloat(opX[randx]), y: CGFloat(opY[randy])).opacity(opac)
                        
                    }
                    //To randomize square position (not to actually change opac)
                    Text("").foregroundColor(Color.white).onReceive(timer, perform: {_ in
                        opac -= 0.1
                        opac += 0.1
                        }).padding(-150)
                    
                    
            
                    
                }
                //Spells out CELL
                    ZStack{
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 30, y: 150)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 120-70, y: 150)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 140-70, y: 150)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60, y: 170)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60, y: 190)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60, y: 210)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60, y: 230)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-40, y: 230)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-20, y: 230)
                    }
                    ZStack{
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 30+85, y: 150)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 120-70 + 85, y: 150)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 140-70 + 85, y: 150)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+85, y: 170)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+85, y: 190)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+85, y: 210)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+85, y: 230)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-40+85, y: 230)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-20+85, y: 230)

                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-20+85, y: 190)
                        
                    }
                    ZStack{
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-20+85-20, y: 190)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 30+170, y: 150)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+170, y: 170)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+170, y: 190)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+170, y: 210)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+170, y: 230)
                        
                        
                    }
                    ZStack{
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 30+170+50, y: 150)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+170+50, y: 170)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+170+50, y: 190)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+170+50, y: 210)
                        Image(systemName: "square.fill").foregroundColor(Color.white).scaleEffect(1.3).position(x: 90-60+170+50, y: 230)

                        
                    }
                    VStack{
                        
                        Spacer()
                        
                        //Play button that gets rid of title screen
                        HStack{
                            Spacer()
                            Button {
                                titleScreen = false
                                soundButton()
                            } label: {
                                Image(systemName: "play.circle.fill").scaleEffect(2.2).foregroundColor(Color.white).padding()
                            }.buttonStyle(.plain)
                        }

                    }
                    
            }
        }
    }
    
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
