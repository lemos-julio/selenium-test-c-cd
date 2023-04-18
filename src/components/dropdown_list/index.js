import './dorpdown_list.css'

const DropDownList = (props) => {


    return (
        <div className="dropDownList">
            <label>{props.label}</label>
            <select onChange={event => props.onChange(event.target.value)}>
            <option value=""></option>
                {props.item.map((item) => {
                   return <option key={item}>{item}</option>
                })}

            </select>
        </div>
    );
}

export default DropDownList