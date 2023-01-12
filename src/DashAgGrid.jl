
module DashAgGrid
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "1.3.1"

include("jl/aggrid.jl")
include("jl/aggridcolumn.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_ag_grid",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_ag_grid.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_ag_grid.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-dashaggrid.js",
    external_url = nothing,
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-dashaggrid.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
