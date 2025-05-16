package main

import (
	"fmt"
	"time"
	"math"
	"github.com/go-vgo/robotgo"
	hook "github.com/robotn/gohook"
)

func main(){
	var option int
	var center [2]int = [2]int{100,100}
	var radius int = 100
	var steps int = 100
	option: for option != -1{
		print_terminal()
		fmt.Print("Choose an option (-1 to finish):")
		fmt.Scan(&option)
		switch option{
		case -1:
			fmt.Println("Killing the process")
			break option
		case 1:
			fmt.Print("Define radius:")
			fmt.Scan(&radius)
		case 2:
			fmt.Print("Define steps:")
			fmt.Scan(&steps)
		case 3:
			fmt.Println("Press 'p' to record")
			evChan := hook.Start()
			defer hook.End()

			for ev := range evChan{
				if string(ev.Keychar) == "p"{
					center[0], center[1] = robotgo.Location()
					break
				}
			}
		case 4:
			fmt.Println("Press p to start")
			evChan := hook.Start()
			defer hook.End()
			for ev := range evChan{
				if string(ev.Keychar) == "p"{
					draw(radius,steps,center)
					break
				}
			}
		default:
			option = 0
			fmt.Println("Please insert a valid option")
		}

	}
}

func print_terminal(){
	menu_string  := `(1) Define radius
(2) Define steps
(3) Define center
(4) Start drawing`
	fmt.Println(menu_string)
}

func draw(radius int, steps int, centers [2]int){
	var pos_x, pos_y, angles []float64

	pos_x = append(pos_x, float64(centers[0]) + (float64(radius) * math.Cos(0 * math.Pi / 180)))
	pos_y = append(pos_y, float64(centers[1]) + (float64(radius) * math.Sin(0 * math.Pi / 180)))

	for i := range steps{
		angles = append(angles, (360/float64(steps)) * float64(i))
	}

	for _, angle := range angles{
		pos_x = append(pos_x, float64(centers[0]) + (float64(radius) * math.Cos(angle * math.Pi/180)))
		pos_y = append(pos_y, float64(centers[1]) + (float64(radius) * math.Sin(angle * math.Pi/180)))
	}

	pos_x = append(pos_x, float64(centers[0]) + (float64(radius) * math.Cos(0 * math.Pi/180)))
	pos_x = append(pos_x, float64(centers[0]) + (float64(radius) * math.Cos(1 * math.Pi/180)))
	pos_y = append(pos_y, float64(centers[1]) + (float64(radius) * math.Sin(0 * math.Pi/180)))
	pos_y = append(pos_y, float64(centers[1]) + (float64(radius) * math.Sin(1 * math.Pi/180)))

	robotgo.Move(int(pos_x[0]),int(pos_y[0]))
	time.Sleep(1 * time.Second)
	robotgo.MouseDown()
	time.Sleep(1 * time.Second)

	for i := range pos_x{
		robotgo.Move(int(pos_x[i]),int(pos_y[i]))
		time.Sleep(10 * time.Millisecond)
	}

	robotgo.MouseUp()

}