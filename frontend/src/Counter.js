import React, { Component } from 'react'

class Counter extends Component {
  // YOUR CODE GOES BELOW
  count: 0;

  render() {
    return (
      <div>
        <label>{count}</label>
        <button>increment</button>
        <button>decrement</button>
      <div/>
    )
  }
}

export default Counter
