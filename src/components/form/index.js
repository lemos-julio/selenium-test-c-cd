import FieldText from '../FieldText'
import './form.css'
import DropDownList from '../dropdown_list'
import Button from '../button/Button'
import { useState } from 'react'


const Form = (props) => {



    const [name, setName] = useState('')
    const [cargo, setCargo] = useState('')
    const [image, setImage] = useState('')
    const [team, setTeam] = useState('')

    const onSave = (evento) => {
        evento.preventDefault()
        props.onColaboratorSubmited({
            name,
            cargo,
            image,
            team
        })

        setName('')
        setCargo('')
        setTeam('')
        setImage('')
    }

    return (


        <section className="form">
            <form onSubmit={onSave}>
                <h2>Preencha os  dados para criar os cards do  colaborador</h2>
                <FieldText
                    label="Nome"
                    placeholder="Digite Seu nome"
                    value={name}
                    onChange={value => setName(value)}
                />

                <FieldText
                    label="Cargo"
                    placeholder="Digite Seu cargo"
                    value={cargo}
                    onChange={value => setCargo(value)} />

                <FieldText
                    label="Imagem"
                    placeholder="Escolha sua imagem"
                    value={image}
                    onChange={value => setImage(value)} />

                <DropDownList
                    label="Time"
                    item={props.teamObj}
                    value={team}
                    onChange={value => setTeam(value)}
                />
                <Button text="Criar Card" />
            </form>
        </section>
    )
}

export default Form