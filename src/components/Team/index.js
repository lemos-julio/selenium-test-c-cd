import Profile from '../cardProfile'
import './team.css'

const Team = (props) => {

    return (

        (props.colaborators.length > 0) ? <section className='TeamSection' style={{ backgroundColor: props.secondaryColor }}>
            <h3 style={{ borderColor: props.primaryColor, color: props.primaryColor }}>{props.teamName}</h3>

            <div className="colaboradores">
                {props.colaborators.map(colaborator => <Profile backgroundColor={props.primaryColor} key={colaborator.name} name={colaborator.name} cargo={colaborator.cargo} image={colaborator.image} />)}
            </div>
        </section>
            : ''
    )
}

export default Team