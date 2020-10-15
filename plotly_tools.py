# Third-party library imports
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
import datetime 
from datetime import date
from datetime import timedelta
def get_main_indicator(daily_totals):

    fig_total = go.Figure()

    fig_total.add_trace(go.Indicator(
        mode="number+delta",
        value=int(daily_totals.sum()),
        title={
            "text": f"Total Cases<br>({daily_totals.index[-1]})<br><span style='font-size:0.6em;color:gray'>Change since last week</span>"},
        delta={'reference': int(daily_totals[:-5].sum()), 'relative': True, 'position': "bottom"},
    ))
    fig_total.update_layout(autosize=True
                            )

    return fig_total


def get_daily_indicator(daily_totals):
    # Daily indicator
    fig_daily = go.Figure()

    fig_daily.add_trace(go.Indicator(
        mode="number+delta",
        value=int(daily_totals[-1]),
        title={
            "text": f"Daily Cases<br>({daily_totals.index[-1]})<br><span style='font-size:0.6em;color:gray'>Change since last week</span>"},
        delta={'reference': int(daily_totals[-6]), 'relative': True, 'position': "bottom"}))

    fig_daily.update_layout(autosize=True
                            )

    return fig_daily

def get_type_totals(type_grouped, type_grouped_yesterday):
    # Type indicators
    fig_type_totals = go.Figure()

    fig_type_totals.add_trace(go.Indicator(
        mode="number+delta",
        value=int(type_grouped[0]),
        #     title = {"text": f"Elementary School Total"},
        domain={'x': [0, 0.1], 'y': [0, 0.25]},
        align="left",
        delta={'reference': int(type_grouped_yesterday[0]), 'relative': True, 'position': "right"}))

    fig_type_totals.add_trace(go.Indicator(
        mode="number+delta",
        value=int(type_grouped[2]),
        #     title = {"text": f"Middle School Total"},
        domain={'x': [0, 0.1], 'y': [0.36, 0.62]},
        align="left",
        delta={'reference': int(type_grouped_yesterday[2]), 'relative': True, 'position': "right"}))

    fig_type_totals.add_trace(go.Indicator(
        mode="number+delta",
        value=int(type_grouped[1]),
        #     title = {"text": f"High School Total"},
        domain={'x': [0, 0.1], 'y': [0.75, 1]},
        align="left",
        delta={'reference': int(type_grouped_yesterday[1]), 'relative': True, 'position': "right"}))

    fig_type_totals.update_layout(
        title={"text": "<span style='font-size:1em;color:black'>Total Cases</span>",
               "yanchor": "middle",
               "xanchor": "center",
               "x": 0.4,
               "y": 0.85})

    fig_type_totals.update_layout(
        annotations=[
            dict(text="<span style='font-size:2em;color:black'>High School</span>",
                 align="right",
                 showarrow=False,
                 x=0.9,
                 y=0.95, ),
            dict(text="<span style='font-size:2em;color:black'>Middle School</span>",
                 align="right",
                 showarrow=False,
                 x=0.9,
                 y=0.48, ),
            dict(text="<span style='font-size:2em;color:black'>Elementary</span>",
                 align="right",
                 showarrow=False,
                 x=0.9,
                 y=0.05, )])

    return fig_type_totals

def get_line_chart(df_series):
    title = 'Total Cases by Date'
    colors = ['rgb(83,190,171)']

    mode_size = [8]
    line_size = [2]

    fig_line = go.Figure()

    fig_line.add_trace(go.Scatter(x=df_series.index, y=df_series, mode='lines',
                                  line=dict(color=colors[0], width=2),
                                  connectgaps=True,
                                  ))

    # endpoints
    fig_line.add_trace(go.Scatter(
        x=[df_series.index[-1]],
        y=[df_series[-1]],
        mode='markers',
        marker=dict(color=colors[0], size=6)
    ))

    fig_line.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=True,
            showticklabels=True,
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)')
        ),
        autosize=True,
        margin=dict(
            autoexpand=False,
            l=20,
            r=20,
            t=20,
        ),
        showlegend=False,
        plot_bgcolor='white'
    )

    fig_line.update_layout(annotations=[dict(xref='paper', yref='paper', x=0.5, y=0.9,
                                             xanchor='center', yanchor='bottom',
                                             text=title,
                                             font=dict(size=26,
                                                       color='rgb(82, 82, 82)'),
                                             showarrow=False)])

    return fig_line


def get_bar_chart(top_schools):
    bar_title = "Schools with Most Positive Cases"

    fig_bar = go.Figure(go.Bar(
        x=top_schools,
        y=top_schools.index,
        orientation='h',
        marker=dict(
            color='rgb(83,190,171)')))

    fig_bar.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=True,
            showticklabels=True,
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)')
        ),
        autosize=True,
        margin=dict(
            autoexpand=True,
            # l=100,
            # r=20,
            # t=100,
        ),
        showlegend=False,
        plot_bgcolor='white'
    )

    fig_bar.update_layout(margin=dict(autoexpand=True),
                          annotations=[dict(xref='paper', yref='paper', x=0.43, y=1,
                                            xanchor='center', yanchor='bottom',
                                            text=bar_title,
                                            font=dict(size=26,
                                                      color='rgb(82, 82, 82)'),
                                            showarrow=False)])

    return fig_bar

def get_map(df_geo):
    # Map
    fig_map = px.scatter_mapbox(df_geo,
                                lat="latitude",
                                lon="longitude",
                                animation_frame='date',
                                animation_group='school',
                                color="Category",
                                size="total",
                                color_discrete_sequence=px.colors.qualitative.Prism,
                                center={"lat": 34.221749,
                                        "lon": -84.135526},
                                zoom=10,
                                # height=00,
                                # width=700,
                                hover_name='school',
                                hover_data=['school', 'total', 'F2F Students & Staff'])
    fig_map.update_layout(mapbox_style="carto-positron")
    fig_map.update_layout(margin={},
                          autosize=True,
                          title=dict(
                              text='Reported Positive Cases',
                              font=dict(
                                  color='black',
                                  size=26),
                              xanchor="center",
                              x=0.5))

    # fig_map['layout']['sliders'][0]['y'] = 1.2
    # fig_map['layout']['updatemenus'][0]['y'] = 1.2

    return fig_map

def stats_results(fig):
    stats_results = px.get_trendline_results(fig)
    return stats_results

def school_chart(df_series, strtitle):
    SCHOOL_ENTITY='School Entity'
    #df_series.sort_values(by='total_positive', ascending=False)
    df_series[SCHOOL_ENTITY] = df_series['school']+" "+df_series['type']
    #removing scools that do not have any covid cases from chart to reduce data.
    df_series.drop(df_series[df_series['total_positive'] < 1].index, inplace = True)
    #dropping columns not required 
    df = df_series.drop(
        columns=['percent_positive', 'F2F Students & Staff', 'total_positive','school'])
    #converting nan to 0
    df.fillna (value=0, inplace=True)
    df.reset_index()

    #flatting data
    df = df.melt([SCHOOL_ENTITY,'type'],var_name='Date', value_name='Count')

    df['Count_csum'] = df.groupby([SCHOOL_ENTITY])['Count'].cumsum()
    print("************")
    df['DateX']=df['Date'].astype('datetime64[ns, US/Eastern]')
    MAX_Y=max(df['Count_csum'])
    min_x=min(df['DateX'])
    max_x=max(df['DateX'])
    df['No_Days_From_Start'] = (df['DateX'] - min_x).dt.days
    #df.drop(df[df['Count_csum'] < 1].index, inplace = True)
    #df.drop(df[df['Count'] < 1].index, inplace = True)
    print(df.info() )
    df.reset_index()
    #df.set_index(['school'])
    print("************")
    print(df)
    #fig_chart=go.Figure()
   
    #fig_chart = px.scatter(df,x='Date', y='Count',color=SCHOOL_ENTITY, size='Count_csum')
    #fig_chart = px.area(df, x='Date', y='Count_csum',
    #                    color=SCHOOL_ENTITY, line_group="type")

    #df = px.data.gapminder()
    #gdp = df['pop'] * df['gdpPercap']
    #fig = px.bar(df, x='year', y=gdp, color='continent', labels={'y':'gdp'},
    #         hover_data=['country'],
    #         title='Evolution of world GDP')
    fig_chart = px.bar(df, x='Date', y='Count', color='type', color_discrete_sequence=px.colors.qualitative.Prism,
     labels={'y':'Count'},
     hover_data=[SCHOOL_ENTITY],title='Reported Positive Cases by School / Department')

    #fig_chart = px.area(df, x='Date', y='Count',
    #                    color=SCHOOL_ENTITY, line_group="type")
     
    #fig_chart = px.scatter(df, x='No_Days_From_Start', y="Count_csum", animation_frame="Date", animation_group="type",
    #                       size="Count_csum", color=SCHOOL_ENTITY, hover_name=SCHOOL_ENTITY,
    #                       size_max=40, range_x=[0, max(df['No_Days_From_Start'])+10], range_y=[0, MAX_Y+4])
    return fig_chart

def get_line_chartv2(df_series, strtitle):
    X_COL='Date Reported'
    df_series.index = pd.to_datetime(
         df_series.index, infer_datetime_format=True)
    df = pd.DataFrame({X_COL: df_series.index,
                       'Count': df_series.values})
    df[X_COL] = pd.to_datetime(
        df[X_COL], infer_datetime_format=True)
    #calculate marker size of +1 to ensure that even 0 value is plotted
    df['marker_size'] = df['Count'] + 1
    
    df.set_index([X_COL])
    #print(df)
    title = strtitle
    colors = ['rgb(83,190,171)']
    black = ['rgb(0,0,0)']
    mode_size = [8]
    line_size = [2]

    #fig_line = go.Figure()
    # works - creates a scatter plot - but lowess trend line is not working.
    #fig_line = px.scatter(df, x=df.index, y='Count', color='Count', size='Count', color_continuous_scale=px.colors.sequential.Viridis, trendline='lowess', range_x=[
    #    min(df['Date Reported'])-timedelta(days=1), max(df['Date Reported'])+timedelta(days=1)])

    fig_line = px.scatter(df, x=df.index, y='Count', size='marker_size', trendline='lowess', 
                          color_continuous_scale=px.colors.qualitative.Prism, color='Count',
    range_x=[min(df['Date Reported'])-timedelta(days=1), max(df['Date Reported'])+timedelta(days=1)])
    fig_line.update_layout(xaxis = dict (
        showline=True, 
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        showticklabels=True,
                     tickmode='array',tickangle=90,
                     tickvals=df.index, title = dict (text='Date'),
        ticktext=[d.strftime('%m/%d/%y') for d in df[X_COL]]))

    fig_line.add_trace(go.Scatter(x=df.index, y=df['Count'], mode='lines+markers+text', text=df['Count'],
                                  line=dict(color=colors[0], width=2), marker=dict(color=black[0], size=df['marker_size'],),
                                    connectgaps=True, line_shape='spline', textposition='top center',name="Count"
                                    ))
    # fig_line = px.scatter(df_series, x=df_series.index,
    #                     y=df_series.values, trendline='lowess')

   

   
    
    #fig_line = px.scatter(x=df_series.index, y=df_series, trendline='lowess', range_x=[
    #    min(df_series.index-timedelta(days=1)), max(df_series.index)+timedelta(days=1)])
    #fig_line.update_layout(xaxis_range=[min(
    #    df['Date Reported'])-timedelta(days=1), max(df['Date Reported'])+timedelta(days=1)])

    #fig_line.add_trace(px.line(x=pd.to_datetime(df_series.index, infer_datetime_format=True),
    #                      y=df_series))

    
                          
    #fig_line = px.scatter(x=df['Date'], y=df['Count'],  trendline='lowess')
    
    #fig_line = px.scatter(df_series, x=df_series.index,
    #                      y=df_series,  trendline='lowess', range_x=[min(df_series.index), max(df_series.index)])
    #fig_line = px.scatter(df_series, x=df_series.index,
    #                       y=df_series,  trendline='lowess')
    

    #fig_line.add_trace(go.Scatter(x=df['Date Reported'], y=df['Count'], mode='lines+markers+text', text=df['Count'],
    #                                line=dict(color=colors[0], width=2), marker=dict(color=black[0], size=df['Count'],),
    #                                 connectgaps=True, line_shape='spline', textposition='top center'
    #                                 ))
    # fig_line.add_trace(go.Scatter(x=df_series.index, y=df_series, mode='lines+markers+text', text=df_series,
    #                               line=dict(color=colors[0], width=2), marker=dict(color=black[0]),
    #                               connectgaps=True, line_shape='spline', textposition='top center',name="Daily Count"
    #                               ))
   
    # This is not required as it can be done with range_x aplied upfront.
    #fig_line.update_layout(xaxis_range=[min(df['Date Reported'])-timedelta(days=1), max(df['Date Reported'])+timedelta(days=1)])

    #endpoints
    #fig_line.add_trace(go.Scatter(
    #    x=[df_series.index[-1]],
    #    y=[df_series[-1]],
    #    mode='markers',
    #    marker=dict(color=colors[0], size=6)
    #))

    # fig_line.update_layout(
    #     xaxis=dict(
    #         showline=True,
    #         showgrid=False,
    #         showticklabels=True,
    #         linecolor='rgb(204, 204, 204)',
    #         linewidth=2,
    #         ticks='outside',
    #         tickfont=dict(
    #             family='Arial',
    #             size=12,
    #             color='rgb(82, 82, 82)',
    #         ),
    #     ),
    #     yaxis=dict(
    #         showgrid=False,
    #         zeroline=False,
    #         showline=True,
    #         showticklabels=True,
    #         tickfont=dict(
    #             family='Arial',
    #             size=12,
    #             color='rgb(82, 82, 82)')
    #     ),
    #     autosize=True,
    #     margin=dict(
    #         autoexpand=False,
    #         l=20,
    #         r=20,
    #         t=20,
    #     ),
    #     showlegend=False,
    #     plot_bgcolor='white'
    # )

    # fig_line.update_layout(annotations=[dict(xref='paper', yref='paper', x=0.5, y=0.9,
    #                                          xanchor='center', yanchor='bottom',
    #                                          text=title,
    #                                          font=dict(size=26,
    #                                                    color='rgb(82, 82, 82)'),
    #                                          showarrow=False)])

    return fig_line
