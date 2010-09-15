${ include("header", conn=conn) }$

${

akills = conn.operserv.akill_list()

}$

<div>

<div class="boxhead">
    <h2>AKILL List</h2>
</div>
<div class="boxbody">

    <table width="100%">
        <tr>
            <th>AKILL ID</th>
            <th width="60%">Mask</th>
            <th>Setter</th>
            <th>Expiry</th>
            <th>Reason</th>
            <th>Actions</th>
        </tr>
${
for akid in akills.keys():
    akill = akills[akid]
    emit('<tr>')
    
    emit('<td>')
    emit(akill['num'])
    emit('</td>')
    
    emit('<td>')
    emit(akill['mask'])
    emit('</td>')
    
    emit('<td>')
    emit(akill['setter'])
    emit('</td>')
    
    emit('<td>')
    expiry = akill['expiry'].replace('expires in ', '')
    emit(expiry)
    emit('</td>')

    emit('<td>')
    emit(akill['reason'])
    emit('</td>')
    
    emit('<td align="right">')
    emit('<a href="remove?id=%d">remove</a>' % akill['num'])
    emit('</td>')
    
    emit('</tr>')
}$      
    </table>

</div>

</div>

${ include("footer") }$
