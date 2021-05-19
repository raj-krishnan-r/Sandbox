#include <SDL.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

class Framework{
public:
    // Contructor which initialize the parameters.
    Framework(int height_, int width_): height(height_), width(width_){
        SDL_Init(SDL_INIT_VIDEO);       // Initializing SDL as Video
        SDL_CreateWindowAndRenderer(width, height, 0, &window, &renderer);
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0);      // setting draw color
        SDL_RenderClear(renderer);      // Clear the newly created window
        SDL_RenderPresent(renderer);    // Reflects the changes done in the
                                        //  window.
    }

    // Destructor
    ~Framework(){
        SDL_DestroyRenderer(renderer);
        SDL_DestroyWindow(window);
        SDL_Quit();
    }
std::vector<std::string> explode(const std::string& str, const char& ch) {
    std::string next;
    std::vector<std::string> result;

    // For each character in the string
    for (std::string::const_iterator it = str.begin(); it != str.end(); it++) {
        // If we've hit the terminal character
        if (*it == ch) {
            // If we have some characters accumulated
            if (!next.empty()) {
                // Add them to the result vector
                result.push_back(next);
                next.clear();
            }
        } else {
            // Accumulate the next character into the sequence
            next += *it;
        }
    }
    if (!next.empty())
         result.push_back(next);
    return result;
}

    void drawer(){
        std::string line;
        std::string loadedFile;
        std::ifstream fileHandle ("source.txt");
        if(fileHandle.is_open()){
            while(getline(fileHandle,line)){
            loadedFile+=line;
            }
            std::vector<std::string> pixels = explode(loadedFile,',');
            for (int x=0;x<width;x++)
            {
                for(int y=0;y<height;y++)
                {
                    int redIS = y*(width*4)+(x*4);
                    std::stringstream red(pixels.at(redIS));
                    std::stringstream green(pixels.at(redIS+1));
                    std::stringstream blue(pixels.at(redIS+2));
                    std::stringstream alpha(pixels.at(redIS+3));
                    int r = 0;
                    red >> r;
                    int g = 0;
                    green >> g;
                    int b = 0;
                    blue >> b;
                    int a = 0;
                    alpha >> a;
                    SDL_SetRenderDrawColor(renderer, r,g,b,a);
                    SDL_RenderDrawPoint(renderer, x, y);
                }
            }
                    SDL_RenderPresent(renderer);
            fileHandle.close();
        }
        else{
            std::cout<<"File closed";
        }

        /*
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
        SDL_RenderDrawPoint(renderer, x, y);
        SDL_RenderPresent(renderer);
        */
    }
    void mouseHead(signed int center_x,signed int center_y){
        /*
        Draws a circle around the mouse, calculate the matrix and paint it.
        */
       
       int radius_ = 20;
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);

        // Drawing circle
        for(int x=center_x-radius_; x<=center_x+radius_; x++){
            for(int y=center_y-radius_; y<=center_y+radius_; y++){
                if((std::pow(center_y-y,2)+std::pow(center_x-x,2)) == std::pow(radius_,2)){

                    SDL_RenderDrawPoint(renderer, x, y);
                }
            }
        }

        // Show the change on the screen
        
        SDL_RenderPresent(renderer);
    }

private:
    int height;     // Height of the window
    int width;      // Width of the window
    SDL_Renderer *renderer = NULL;      // Pointer for the renderer
    SDL_Window *window = NULL;      // Pointer for the window
};

int main(int argc, char * argv[]){

    // Creating the object by passing Height and Width value.
    Framework fw(667, 1000);

    // Calling the function that draws circle.
    fw.drawer();

    SDL_Event event;    // Event variable

    // Below while loop checks if the window has terminated using close in the
    //  corner.
    while(!(event.type == SDL_QUIT)){
        SDL_Delay(1);  // setting some Delay
          // Catching the poll event.
        while(SDL_PollEvent(&event))
        if(event.type == SDL_MOUSEMOTION){
            fw.mouseHead(event.motion.x,event.motion.y);
        }
    }
    
}