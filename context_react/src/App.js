import React, { useContext, useEffect, useState } from 'react';
const ThemeContext = React.createContext({title:"Black"});

const App=()=>{
  const [bound,setBound]=useState({title:"RED"});

  return(
    //Context Idea is this
    <ThemeContext.Provider value={bound,setBound}>
      <Toolbar/>
    </ThemeContext.Provider>
  );
}
const Toolbar=()=>{
const [bound,setBound] = useContext(ThemeContext);
return(
  <div>Datum : {bound.title}</div>
);
}
export default App;