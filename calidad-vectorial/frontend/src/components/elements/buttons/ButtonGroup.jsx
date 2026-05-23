import React from "react"
import"./Button.css"

export const ButtonGroup = ({ children }) => {
    return (
        <div className="btn-group">{children}</div>
    )
}