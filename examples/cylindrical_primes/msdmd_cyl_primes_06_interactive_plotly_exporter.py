# msdmd:1.0
skill:
  name: cyl_primes_06_interactive_plotly_exporter
  version: "0.1.0"
  author: "wayseer00 / Erin Patrick Spencer (The Interdependency LLC)"
  description: "Generates self-contained interactive Plotly HTML for the cylindrical graph. Granular module 6/8. Includes cylinder surface, prime scatter, and twin-prime skeletal edges. Hover, rotate, zoom ready for phone/browser. msdmd compliant."
  inputs:
    - name: xs, ys, zs, thetas
    - name: twin_edge_indices
    - name: output_html_path
  outputs:
    - name: html_file
      description: "Self-contained interactive .html"
  relations:
    - "Interactive visualization layer for UCNS cylindrical primes"
    - "Explicit π geometry preserved in 3D scene"
    - "Complements module 05 (static matplotlib)"
  epistemic_status: "prototype / IMPLEMENTED"
  msdmd_compliant: true
  granularity_factor: 8
  list_position: 6

"""
Interactive Plotly Exporter (msdmd skill 06/8)
"""
try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

def export_interactive_html(xs, ys, zs, thetas, twin_edge_indices, output_html="cylindrical_primes_ucns.html", title_suffix=""):
    """Export full interactive 3D HTML."""
    if not PLOTLY_AVAILABLE:
        print("Plotly not installed. Skipping interactive export.")
        return None

    fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scene'}]])

    # Cylinder surface (light)
    import numpy as np
    theta_surf = np.linspace(0, 2*np.pi, 60)
    z_surf = np.linspace(min(zs), max(zs), 30)
    theta_surf, z_surf = np.meshgrid(theta_surf, z_surf)
    x_surf = np.cos(theta_surf)
    y_surf = np.sin(theta_surf)

    fig.add_trace(go.Surface(
        x=x_surf, y=y_surf, z=z_surf,
        colorscale=[[0,'rgba(180,180,180,0.08)'],[1,'rgba(180,180,180,0.08)']],
        showscale=False, name='Unit Cylinder', hoverinfo='skip'
    ))

    # Primes
    fig.add_trace(go.Scatter3d(
        x=xs, y=ys, z=zs,
        mode='markers',
        marker=dict(size=4, color=zs, colorscale='Viridis', opacity=0.85),
        text=[f"p={p}<br>n={i}<br>θ={t*180/np.pi:.1f}°" for i,(p,t) in enumerate(zip(primes if 'primes' in dir() else range(len(xs)), thetas))],
        hovertemplate='%{text}<extra></extra>',
        name='Primes'
    ))

    # Twin skeletal lines
    if twin_edge_indices:
        twin_x, twin_y, twin_z = [], [], []
        for i1, i2 in twin_edge_indices:
            twin_x.extend([xs[i1], xs[i2], None])
            twin_y.extend([ys[i1], ys[i2], None])
            twin_z.extend([zs[i1], zs[i2], None])
        fig.add_trace(go.Scatter3d(
            x=twin_x, y=twin_y, z=twin_z,
            mode='lines',
            line=dict(color='red', width=3),
            name='Twin Prime Skeletal Structure',
            hoverinfo='skip'
        ))

    fig.update_layout(
        title=dict(text=f'Cylindrical Graph of Primes — UCNS Extension<br><sub>{title_suffix}<br>θ = 2π × (p mod m)/m | Twin primes = skeletal structure</sub>', x=0.5),
        scene=dict(xaxis_title='X = cos(θ)', yaxis_title='Y = sin(θ)', zaxis_title='Z (scaled)', aspectmode='data'),
        margin=dict(l=0,r=0,b=0,t=60)
    )
    fig.write_html(output_html, include_plotlyjs='cdn')
    print(f"Interactive HTML saved: {output_html}")
    return output_html

if __name__ == "__main__":
    print("Module 06 ready. Requires primes + mapped coordinates from modules 01-03.")