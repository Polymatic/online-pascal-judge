import React, { useState, useEffect } from 'react'
import service from './backend'
import './App.css';

const Output = ({obj}) => {
  console.log(obj.stdout, obj.stderr)

  if (obj.stdout !== "") {
    return (
      <div>
        <br></br>
        <textarea style={{backgroundColor: "lightgreen"}} rows="20" value = {obj.stdout} />
      </div>
      )
  } else {
    console.log("hererrerrerrererer")
    return (
      <div>
        <br></br>
        <textarea style={{backgroundColor: "#ff8080"}} rows="20" value = {obj.stderr} />
      </div>
      )
  }
}

const Languages = (props) => {
  const arr = props.availableLanguages.map((lang, i) => <option key={i} value={lang}>{lang}</option>)
  return  (
    <div>
      <h3 >Select Programming Language</h3>
      <select id="Language" onChange = {props.handleLangChange}>
        {arr}
      </select>
    </div>
  )
}


function App() {
  const [availableLanguages, setAvailableLangues] = useState([])
  const [newCode, setCode] = useState('Write code here')
  const [lang, setLang] = useState('pascal')
  const [output, setOutput] = useState({stdout: "Output will be presented here", stderr:""})


  useEffect(() => {
    service.getAvailableLanguages()
      .then(data => {setAvailableLangues(data)})
  }, [])

  // console.log(lang, newCode)
  const handleLangChange = event => {
    setLang(event.target.value)

  }

  const handleCodeChange = event => {
    // console.log(newCode)
    setCode(event.target.value)
  }

  const executeCodeFoo = event => {
    event.preventDefault()

    service.sendCode(lang, newCode).then(data => {
      console.log(data)
      setOutput(data)
    })
  }

  return (
    <div>
      <h1>ONLINE INTERPRETER</h1>
      <Languages availableLanguages={availableLanguages} handleLangChange={handleLangChange} />
      <br></br>
      <form onSubmit = {executeCodeFoo}>
        <div>
          <textarea rows="10" value = {newCode}
          onChange = {handleCodeChange}/>
        </div>
        <br></br>
        <button type="sumbit">RUN</button>
      </form>

      <div>
        <Output obj={output}/>
      </div>
    </div>

  );
}

export default App;
