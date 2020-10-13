import React, { useState } from 'react';
import axios from 'axios'

function Cell(props) {
  const {row} = props
  const [val, setVal] = useState(row.value)
  const editValue = (newValue) => {
    const url = 'http://127.0.0.1:8000/api/table/edit_table/'
    const data = {'x_axis': row.x, 'y_axis': row.y, 'value': newValue}
    axios.post(url, data).then(setVal(newValue))
  }
  React.useEffect(() => {
    setVal(row.value)
  }, [row.value])
  return (
    <form>
      <label>
        <input type="text" value={val} onChange={event => editValue(event.target.value)} />
      </label>
    </form>
  )
}


function App() {
  const [tableData, setTableData] = useState([{}])
  const xAxis = [0, 1, 2, 3, 4, 5, 6, 7]
  const yAxis = [0, 1, 2, 3, 4, 5, 6, 7]

  React.useEffect(() => {
    const url = 'http://127.0.0.1:8000/api/table/get_table/'
    axios.get(url).then(response => {
      setTableData(response.data)
     }).catch()
  }, [])

  const getData = (x, y) => {
    for (let item of tableData) {
      if (item['x_axis'] === x && item['y_axis'] === y) {
        return item['value']
      }
    }
    return ''
  }
  return (
    <div>
      {yAxis.map((y) => {
        return (
          <div style={{display: 'flex'}}>
            {xAxis.map((x) => {
              let row = {'x': x, 'y': y, 'value': getData(x, y)}
              return (
                <Cell row={row} />
              )
            })}
          </div>
        )
      })}
    </div>
  )


}
export default App
