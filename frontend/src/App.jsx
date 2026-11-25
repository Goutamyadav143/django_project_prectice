import React,{useState,useEffect} from 'react'
import './App.css';

export default function App() {
  let [FoodIteam,setFooditeam]= useState([]);

  async function getData (){
    let res = await fetch("http://127.0.0.1:8000/food/menu")
   let data = await res.json();
    setFooditeam(data.data)
  }




  useEffect(()=>
  {
    getData()
  },[]
  )
  return (
    <div>
      <div id='hedding'>
        <h1>FOOD APP</h1>
      </div>
      <div id='Grid'>
        {
          FoodIteam.map((f)=>(
            <div className='card'>
              <img src={f.image} alt={f.name} />
              <h3>{f.name}</h3>
              <p>{f.price}</p>

            </div>
            
          ))
        }
      </div>
    </div>
  )
}
