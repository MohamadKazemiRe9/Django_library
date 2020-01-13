import React from 'react'
import ReactDOM from 'react-dom'
import Header from './layout/Header'

class App extends React.Component{
    render(){
        return(
            <>
            <Header/>
            <h1>welcom to react django</h1>
            <h4>thank's for watching</h4>
            </>
        )
    }
}

ReactDOM.render(<App/>,document.getElementById('root'))