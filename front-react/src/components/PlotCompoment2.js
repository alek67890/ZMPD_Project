import React from 'react'
// import ReactDOM from 'react-dom'
import { ScatterPlot, LineChart, LinearYAxis, LinearXAxis} from 'reaviz';


class PlotCompoment2 extends React.Component {
  constructor(props){
    super(props);
    let temp = [[145.0, 215.0],    [151.0, 264.0],   [159.0, 261.0],    [130.0, 254.0],    [128.0, 252.0],    [163.0, 247.0],   [146.0, 246.0],    [161.0, 242.0],    [142.0, 239.0],    [163.0, 236.0],    [148.0, 232.0],    [128.0, 231.0],    [156.0, 217.0],    [129.0, 214.0],    [146.0, 208.0],    [164.0, 208.0],    [141.0, 206.0],    [147.0, 193.0],    [164.0, 193.0],    [129.0, 189.0],    [155.0, 185.0],    [139.0, 182.0]]
    let data =  temp.map((item) => {
      return { key:item[0], data:item[1]}
    })
    let temp2 = [[145, 215],[146, 208],[164, 193],[155, 185], [139, 182], [141, 206], [145, 215]]
    let data2 =  temp2.map((item) => {
      return { key:item[0], data:item[1]}
    })
  
    this.state = {
        data : data,
        data2 : data2,
      };
}

//   componentDidMount(){

 
//     // data = [
//     //   { key: new Date('11/29/2019'), data: 13 },
//     //   { key: new Date('11/30/2019'), data: 13 },
//     //   { key: new Date('12/1/2019'), data: 13 },
//     // ]
//   this.setState({data : data});
// }

  render () {
    console.log(this.state.data)
    return <div className="ui segment">
        <div className='message-box'>
          Hello World 
          <br/>
          <ScatterPlot
            height={300}
            width={300}
            data={this.state.data}
            yAxis={<LinearYAxis
              type="value"
              scaled={true}
              domain={[160, 260]}
            />}
            xAxis={<LinearXAxis
              type="value"
              scaled={true}
              domain={[120, 165]}
            />}
          />

          <LineChart
              width={350}
              height={250}
              data={this.state.data2}
              // gridlines={<GridlineSeries line={<Gridline direction="all" />}
              yAxis={<LinearYAxis
                type="value"
                scaled={true}
                domain={[160, 260]}
              />}
              xAxis={<LinearXAxis
                type="value"
                scaled={true}
                domain={[120, 165]}
              />}
            />
      </div>
    </div>
  }
}

export default PlotCompoment2;